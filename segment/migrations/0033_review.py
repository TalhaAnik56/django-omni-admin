# Generated by Django 5.0.6 on 2024-07-02 11:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_guest_created_at_staff'),
        ('segment', '0032_rename_distance_from_hotel_touristspot_distance_from_hotel_in_km_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.CharField(blank=True, max_length=900, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.guest')),
            ],
        ),
    ]