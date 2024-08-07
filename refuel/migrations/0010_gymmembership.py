# Generated by Django 5.0.6 on 2024-07-02 17:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refuel', '0009_gym_discount_in_percentage'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')], default='Pending', max_length=15)),
                ('name', models.CharField(max_length=99)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(100)])),
                ('mobile', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('monthly_fees', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('additional_info', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='refuel.gym')),
            ],
        ),
    ]
