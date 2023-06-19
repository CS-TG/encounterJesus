from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theWebsite.urls')),
    path('blog/', include('blog.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
