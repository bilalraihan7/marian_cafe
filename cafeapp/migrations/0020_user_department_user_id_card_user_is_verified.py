# Generated by Django 4.2.7 on 2024-01-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0019_remove_booking_fare_remove_booking_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(default='nothing', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='id_card',
            field=models.ImageField(default='nothing', upload_to='idcard/'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='Is Verified'),
        ),
    ]