from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

class UserDetail(viewsets.ViewSet):
    def list(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)
        queryset = Profile.objects.all()
        profile = get_object_or_404(queryset, user=user)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

    def update(self, request, pk=None):
        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
