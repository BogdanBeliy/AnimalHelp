from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.profiles.serializers import ProfileSerializer
from apps.profiles.models import Profile


# Create your views here.
class ProfileView(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


profile_view = ProfileView.as_view({'get': 'list'})
