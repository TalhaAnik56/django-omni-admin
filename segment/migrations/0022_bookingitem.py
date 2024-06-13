# Generated by Django 5.0.6 on 2024-06-13 03:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segment', '0021_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount_in_percentage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='segment.room')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segment.booking')),
                ('room_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='segment.roomcategory')),
            ],
            options={
                'unique_together': {('booking', 'assigned_room')},
            },
        ),
    ]