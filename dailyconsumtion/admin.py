from django.contrib import admin

# Register your models here.

from .models import DailyConsumption, CapturedFood


admin.site.register(DailyConsumption)
admin.site.register(CapturedFood)
