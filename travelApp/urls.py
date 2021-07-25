from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('packages', views.packages, name='packages'),
    path('blog', views.blog, name='blog'),
  path('services', views.services, name='services'),
path('terms', views.terms, name='terms'),

]
