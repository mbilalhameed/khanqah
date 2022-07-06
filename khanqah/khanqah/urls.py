from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'khanqah-admin-site/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth', include('djoser.urls.jwt')),
    path('api/v1/profile', include('apps.profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Khankah Admin"
admin.site.site_title = "Khankah Admin Portal"
admin.site.index_title = "Welcome to Khankah Portal"
