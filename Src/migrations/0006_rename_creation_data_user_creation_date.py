# Generated by Django 3.2.4 on 2021-07-07 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0005_user_access_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='creation_data',
            new_name='creation_date',
        ),
    ]
