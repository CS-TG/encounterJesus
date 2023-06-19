from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Testimony', 'Testimony'),
        ('Encouragement', 'Encouragement'),
        ('General', 'General'),
    ]
    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('blog:article-detail', args=(str(self.id),) )