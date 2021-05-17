from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import DailyConsumption
from .serializers import DailyConsumptionSerializer
from google.cloud import storage
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

class DailyConsumptionList(viewsets.ViewSet):
    def list(self, request):
        dailyconsumption = DailyConsumption.objects.all()
        serializer = DailyConsumptionSerializer(dailyconsumption, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = DailyConsumptionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ this retrieve method get list of data based on user_id  """
        queryset = DailyConsumption.objects.filter(user_id=pk)
        serializer = DailyConsumptionSerializer(queryset, many=True)

        return Response(serializer.data)