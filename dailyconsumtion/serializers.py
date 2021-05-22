from rest_framework import serializers
from .models import DailyConsumption, CapturedFood

class DailyConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyConsumption
        fields = '__all__'


class CapturedFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturedFood
        fields = '__all__'
