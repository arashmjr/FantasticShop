# Generated by Django 3.2.4 on 2021-07-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0010_auto_20210707_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_level',
            field=models.IntegerField(default=-1.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(default=-1.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.BigIntegerField(default=-1.0),
            preserve_default=False,
        ),
    ]
