# Generated by Django 5.0.6 on 2024-06-28 12:40

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refuel', '0003_restaurant_discount_in_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=15)),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=14)),
                ('number_of_people', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.TimeField()),
                ('additional_information', models.TextField(blank=True, null=True)),
                ('total_bill', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=15)),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='refuel.restaurant')),
            ],
        ),
    ]