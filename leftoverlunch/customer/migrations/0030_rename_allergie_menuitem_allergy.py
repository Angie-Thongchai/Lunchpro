# Generated by Django 4.2.5 on 2023-10-17 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0029_rename_allergie_allergy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='allergie',
            new_name='allergy',
        ),
    ]
