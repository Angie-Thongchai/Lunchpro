# Generated by Django 4.2.5 on 2023-10-22 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0051_ordermodel_telephone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='email',
        ),
    ]