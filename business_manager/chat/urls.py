from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),  # Rota principal do chat
]