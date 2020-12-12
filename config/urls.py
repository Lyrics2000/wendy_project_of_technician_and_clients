
from django.contrib import admin
from django.urls import path
from config.settings.development import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]
if DEBUG:
    urlpatterns  =  urlpatterns + static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns  =  urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)