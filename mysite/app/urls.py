
from django.urls import path
from app import views

urlpatterns = [
    path('', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
]
