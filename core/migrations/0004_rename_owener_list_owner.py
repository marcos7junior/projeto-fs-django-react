# Generated by Django 4.1.1 on 2022-10-03 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='owener',
            new_name='owner',
        ),
    ]