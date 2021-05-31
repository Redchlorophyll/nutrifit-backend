from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import DailyConsumption, CapturedFood
from .serializers import DailyConsumptionSerializer, CapturedFoodSerializer
from google.cloud import storage
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
import requests
import json
import os


# Create your views here.

class DailyConsumptionList(viewsets.ViewSet):
    #this variable is used to make sure to access this class user must be authenticated
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        """ POST list of food. can be more then one using list """

        list = []
        foodsconsumed = request.data

        #iterate request first to get each data in list
        for food in foodsconsumed:
            serializer = DailyConsumptionSerializer(data=food)
            list.append(food)

            if serializer.is_valid():
                serializer.save()
                serializers = serializer

        return Response(list, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """ this retrieve method get list of data based on user_id  """
        queryset = DailyConsumption.objects.filter(user_id=pk).order_by('-id')
        serializer = DailyConsumptionSerializer(queryset, many=True)

        return Response(serializer.data)


class FoodJourney(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, userid=None):
        """ GET sum of food eaten for each day for 30 days  """
        foodjourney = DailyConsumption.objects.values("date_time_consumed").annotate(
                                                calories=Sum('calories'),
                                                total_fat=Sum('total_fat'),
                                                saturated_fat=Sum('saturated_fat'),
                                                cholesterol=Sum('cholesterol'),
                                                sodium=Sum('sodium'),
                                                fiber=Sum('fiber'),
                                                sugar=Sum('sugar'),
                                                protein=Sum('protein'),
                                                ).filter(user_id=userid).order_by('-date_time_consumed')[:30]

        return Response(foodjourney)



class FoodName(APIView):
    #this variable is used to make sure to access this class user must be authenticated
    permission_classes = (IsAuthenticated,)

    def get(self, request, userid=None, date=None):
        """ GET list of food eaten in specific day """
        foodjourney = DailyConsumption.objects.values('food_name',
                                                      'quantity',
                                                      'CapturedFood_id',
                                                      'time_food_consumed',
                                                      'date_time_consumed',
                                                      'serving_size',
                                                      'calories',
                                                      'total_fat',
                                                      'saturated_fat',
                                                      'cholesterol',
                                                      'sodium',
                                                      'carbonhydrates',
                                                      'fiber',
                                                      'sugar',
                                                      'protein').filter(user_id=userid, date_time_consumed=date).order_by("-id")

        return Response(foodjourney)



class MonthlyFood(APIView):
    def get(self, request, userid=False, year=False, month=False):
        foodjourney = DailyConsumption.objects.filter(user_id=userid,
                                                      date_time_consumed__year=year,
                                                      date_time_consumed__month=month)

        serializer = DailyConsumptionSerializer(foodjourney, many=True)

        return Response(serializer.data)



class CapturedImageWithPrediction(APIView):
    #this variable is used to make sure to access this class user must be authenticated
    permission_classes = (IsAuthenticated,)

    def post(self, request, model_name=None):
        """ uplod image to google cloud storage and get prediction. receive image property consist id, url and upload date and also prediction result """
        serializer = CapturedFoodSerializer(data=request.data)
        prediction_output = ''

        if serializer.is_valid():
            model_url = os.environ.get('NUTRIFIT_ML_URL')
            model_endpoint = "{}/v1/object-detection/{}".format(model_url, model_name)
            response = request.FILES.get('image_url')
            object = { 'image' : response}
            modeloutput = requests.post(model_endpoint, files=object)

            if modeloutput.status_code == 200:
                prediction_output = json.loads(modeloutput.content)
            else:
                prediction_output = 'you insert wrong model name! try again'

            serializer.save()

            output = {}
            output['image_property'] = serializer.data
            output['prediction'] = prediction_output



            return Response(output, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CapturedImage(APIView):
    #this variable is used to make sure to access this class user must be authenticated
    permission_classes = (IsAuthenticated,)

    def post(self, request, userid=None):
        """ uplod image to google cloud storage. receive id to bind to food list  """
        serializer = CapturedFoodSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class getImage(APIView):
    #this variable is used to make sure to access this class user must be authenticated
    permission_classes = (IsAuthenticated,)

    def get(self, request, imageid=None):
        """  get food image url previously uploaded in google cloud storage with food image id """
        image = CapturedFood.objects.get(id=imageid)
        serializer = CapturedFoodSerializer(image)

        return Response(serializer.data)
