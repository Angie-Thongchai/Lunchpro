# Generated by Django 4.2.5 on 2023-10-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_remove_menuitem_is_active_alter_menuitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='collect',
            field=models.BooleanField(default=False),
        ),
    ]
