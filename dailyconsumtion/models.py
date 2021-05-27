from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import os

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'media/uploads/'
    # get file extension. like .png, .jpg or else that image extension
    ext = filename.split('.')[-1]
    name = filename.split('.')[0]
    # get filename
    new_name = "{}.{}".format(name, uuid4())
    filename = "{}.{}".format(new_name, ext)

    #return the whole path to the file
    return os.path.join(upload_to, filename)



class CapturedFood(models.Model):
    upload_date = models.DateField(auto_now_add=True)
    image_url = models.ImageField(upload_to=path_and_rename)

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
    serving_size = models.DecimalField(max_digits=10, decimal_places=2)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    total_fat = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat = models.DecimalField(max_digits=10, decimal_places=2)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2)
    sodium = models.DecimalField(max_digits=10, decimal_places=2)
    carbonhydrates = models.DecimalField(max_digits=10, decimal_places=2)
    fiber = models.DecimalField(max_digits=10, decimal_places=2)
    sugar = models.DecimalField(max_digits=10, decimal_places=2)
    protein = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return "{}. {}".format(self.id, self.food_name)
