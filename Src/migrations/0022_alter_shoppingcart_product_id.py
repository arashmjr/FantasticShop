# Generated by Django 3.2.4 on 2021-07-11 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0021_alter_shoppingcart_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='product_id',
            field=models.BigIntegerField(),
        ),
    ]
