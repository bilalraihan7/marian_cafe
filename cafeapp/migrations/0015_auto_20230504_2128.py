# Generated by Django 3.2 on 2023-05-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0014_booking_date_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]