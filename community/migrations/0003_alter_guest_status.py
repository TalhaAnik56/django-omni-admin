# Generated by Django 5.0.6 on 2024-06-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_guest_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=9),
        ),
    ]
