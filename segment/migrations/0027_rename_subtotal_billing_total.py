# Generated by Django 5.0.6 on 2024-06-13 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('segment', '0026_rename_rack_rate_bookingitem_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='subtotal',
            new_name='total',
        ),
    ]