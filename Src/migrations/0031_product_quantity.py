# Generated by Django 3.2.4 on 2021-07-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0030_cartproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.BigIntegerField(default=-1.0),
            preserve_default=False,
        ),
    ]