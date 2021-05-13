from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Daily_consumption(models.Model):
    food_name = models.CharField(max_length=90)
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True,blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_food_consumed = models.DateTimeField(auto_now_add=True)
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
