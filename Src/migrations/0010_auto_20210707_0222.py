# Generated by Django 3.2.4 on 2021-07-07 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0009_alter_user_creation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='access_level',
        ),
        migrations.RemoveField(
            model_name='user',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postal_code',
        ),
    ]
