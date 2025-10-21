from .views import profile_view
from django.urls import path

urlpatterns= [
    path("me/", profile_view, name='profile'),
]