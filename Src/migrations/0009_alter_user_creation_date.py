# Generated by Django 3.2.4 on 2021-07-07 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0008_remove_user_confirm_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
