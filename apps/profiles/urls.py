from django.urls import path
from apps.profiles.views import profile_view

urlpatterns = [
    path('', profile_view)
]