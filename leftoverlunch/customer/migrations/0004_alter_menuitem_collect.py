# Generated by Django 4.2.5 on 2023-10-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_menuitem_collect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='collect',
            field=models.CharField(max_length=100),
        ),
    ]