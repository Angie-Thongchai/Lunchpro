# Generated by Django 4.2.5 on 2023-10-18 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0037_orderitem_remove_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='complete',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
