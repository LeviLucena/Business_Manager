from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Novidade aqui!
    path('', include('core.urls')),
    path('chat/', include('chat.urls')),
    path('accounts/logout/', TemplateView.as_view(template_name='registration/logged_out.html')),
]