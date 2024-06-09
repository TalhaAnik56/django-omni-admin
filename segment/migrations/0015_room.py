# Generated by Django 5.0.6 on 2024-06-08 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segment', '0014_alter_roomcategory_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Out Of Order', 'Out Of Order'), ('Occupied', 'Occupied'), ('Booked', 'Booked')], default='Active', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('room_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segment.roomcategory')),
            ],
        ),
    ]