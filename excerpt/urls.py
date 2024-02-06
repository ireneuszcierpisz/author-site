from . import views
from django.urls import path

urlpatterns = [
    path('', views.excerpt_from, name='excerpt'),
]
