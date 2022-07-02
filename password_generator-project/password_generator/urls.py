
from generator import views
from django.urls import path

urlpatterns = [
    path('',views.generator, name='generator' ),
    path('password', views.password, name='password'),
    path('about', views.about, name='about'),
    
]
