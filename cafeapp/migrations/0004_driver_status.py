# Generated by Django 3.2 on 2023-04-11 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0003_remove_driver_car_model_remove_driver_license_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='status',
            field=models.CharField(default='Not Verified', max_length=20),
        ),
    ]