from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.utils import json
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from account.models import Profile
# Create your views here.


class DummyView(APIView):
    """ class to check whatever user already has token to access endpoint or not. """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """ get congratulation status when you succesfully logged in """
        content = {'status': "congrats,you sucessfully login with your gmail account!"}
        return Response(content)



class GoogleView(APIView):
    """ class to auth google user """
    def post(self, request):
        """ function to log in or sign up using google account """
        # retrieve post request data
        data = {
            'email' : request.data.get('email'),
            'username' : request.data.get('username'),
            'profile_pic' : request.data.get('profile_pic'),
        }

        try:
            user = User.objects.get(email=data['email'])
            profile = Profile.objects.get(user=user)
        except User.DoesNotExist:
            user = User()
            user.username = data['username']
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data["email"]
            user.save()

            profile = Profile.objects.get(user=user)
            profile.profile_pic = data['profile_pic']
            profile.save()

        token = RefreshToken.for_user(user)
        response = {}

        response['user_id'] = user.id
        response['username'] = user.username
        response['access_token'] = str(token.access_token)
        response['refresh_token'] = str(token)
        response['profile_pic'] = profile.profile_pic

        return Response(response)
