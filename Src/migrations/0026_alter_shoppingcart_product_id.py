# Generated by Django 3.2.4 on 2021-07-11 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0025_auto_20210711_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Src.product'),
        ),
    ]