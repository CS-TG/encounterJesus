from django.urls import path
from .views import PostView, PostDetailedView, AddPostView, user_login, authenticate_user, register, logout_view

app_name = 'blog'
urlpatterns = [
    path('', PostView.as_view(), name="blog"),
    path('login/', user_login, name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('authenticate_user/', authenticate_user, name='authenticate_user'),
    path('article/<int:pk>', PostDetailedView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name='add_post')
]