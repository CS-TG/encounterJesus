from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


def user_login(request):
    """
    Displays the login page.
    """
    return render(request, 'login.html')


def authenticate_user(request):
    """
    Authenticates the user and redirects to the appropriate page based on the authentication result.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(reverse('blog:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('blog:add_post'))


def register(request):
    """
    Handles the user registration process.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    """
    Logs out the user and redirects to the index page.
    """
    logout(request)
    return redirect('theWebsite:index')


class PostView(ListView):
    """
    Displays a list of posts.
    """
    model = Post
    template_name = 'blog.html'


class PostDetailedView(DetailView):
    """
    Displays the details of a specific post.
    """
    model = Post
    template_name = 'post_details.html'


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class AddPostView(LoginRequiredMixin, View):
    """
    Handles the creation of new posts.
    """
    login_url = 'blog:login'
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get(self, request):
        """
        Displays the form for adding a new post.
        """
        form = PostForm(initial={'author': request.user})  # Set the initial value of the author field
        return render(request, 'add_post.html', {'form': form})

    def post(self, request):
        """
        Handles the submission of the form for adding a new post.
        """
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:blog')  # Redirect to the list of posts

        return render(request, 'add_post.html', {'form': form})

    def get_form(self, form_class=None):
        """
        Returns the form instance with the author field hidden.
        """
        form = super().get_form(form_class)
        form.fields['author'].widget = forms.HiddenInput()  # Hide the author field
        return form

    def form_valid(self, form):
        """
        Sets the logged-in user as the author of the post.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)