# Generated by Django 3.2.4 on 2021-07-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0004_auto_20210707_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_level',
            field=models.IntegerField(default=-1.0),
            preserve_default=False,
        ),
    ]