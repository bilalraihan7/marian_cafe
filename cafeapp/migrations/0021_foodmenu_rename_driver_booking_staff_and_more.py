# Generated by Django 4.2.7 on 2024-01-27 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0020_user_department_user_id_card_user_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodmenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ftype', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='vehicles/')),
                ('rate', models.IntegerField(null=True)),
                ('status', models.CharField(default='not booked', max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='driver',
            new_name='staff',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='dropoff_location',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='pickup_location',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='vehicle',
        ),
        migrations.RenameModel(
            old_name='Driver',
            new_name='Staff',
        ),
        migrations.DeleteModel(
            name='vehicle',
        ),
        migrations.AddField(
            model_name='foodmenu',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeapp.staff'),
        ),
        migrations.AddField(
            model_name='booking',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cafeapp.foodmenu'),
        ),
    ]