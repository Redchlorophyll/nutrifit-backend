from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserDetail(viewsets.ViewSet):
    #this variable is used to make sure to access this class user must be authenticated
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        """ get profile data like user, weight, height, birth_date """
        user = User.objects.get(pk=pk)
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, user=user)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

    def update(self, request, pk=None):
        """ update profile data like user, weight, height, birth_date """
        user = User.objects.get(pk=pk)
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
