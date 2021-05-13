# Generated by Django 3.2.2 on 2021-05-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyconsumtion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_consumption',
            name='calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='carbonhydrates',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='cholesterol',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='fiber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='food_name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='protein',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='saturated_fat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='serving_size',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='sodium',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='sugar',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='daily_consumption',
            name='total_fat',
            field=models.IntegerField(),
        ),
    ]
