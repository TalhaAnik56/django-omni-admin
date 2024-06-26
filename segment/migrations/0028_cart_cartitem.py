# Generated by Django 5.0.6 on 2024-06-24 02:07

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segment', '0027_rename_subtotal_billing_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segment.cart')),
                ('room_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segment.roomcategory')),
            ],
            options={
                'unique_together': {('cart', 'room_category')},
            },
        ),
    ]
