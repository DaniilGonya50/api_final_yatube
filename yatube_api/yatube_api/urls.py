from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api.constants import API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'api/{API_VERSION}/', include('djoser.urls')),
    path(f'api/{API_VERSION}/', include('djoser.urls.jwt')),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
