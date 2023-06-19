from django.urls import path
from .views import index, testimonies

app_name = 'theWebsite'

urlpatterns = [
    path('', index, name='index'),
    path('testimonies/', testimonies, name='testimonies')
]
