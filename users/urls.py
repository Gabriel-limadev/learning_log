"""Define padrões de URL para users"""

from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Página de Login
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register')
]
