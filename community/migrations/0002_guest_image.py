# Generated by Django 5.0.6 on 2024-06-05 21:45

import general_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='community/images', validators=[general_app.validators.image_max_size]),
        ),
    ]
