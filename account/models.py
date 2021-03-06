from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_pic = models.CharField(null=True, blank=True, max_length=255)
    # location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # weight = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
