from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CapturedFood(models.Model):
    image_url = models.ImageField(upload_to='media/uploads/')

    def __str__(self):
        return "{}. {}".format(self.id, self.image_url)



class DailyConsumption(models.Model):
    food_name = models.CharField(max_length=90)
    quantity = models.IntegerField()
    # image_url = models.ImageField(upload_to="media/uploads/", null=True, blank=True)
    CapturedFood_id = models.ForeignKey(CapturedFood, on_delete = models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_food_consumed = models.DateTimeField(auto_now_add=True)
    date_time_consumed = models.DateField(auto_now_add=True)
    serving_size = models.IntegerField()
    calories = models.IntegerField()
    total_fat = models.IntegerField()
    saturated_fat = models.IntegerField()
    cholesterol = models.IntegerField()
    sodium = models.IntegerField()
    carbonhydrates = models.IntegerField()
    fiber = models.IntegerField()
    sugar = models.IntegerField()
    protein = models.IntegerField()


    def __str__(self):
        return "{}. {}".format(self.id, self.food_name)
