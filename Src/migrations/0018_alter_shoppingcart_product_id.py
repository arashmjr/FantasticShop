# Generated by Django 3.2.4 on 2021-07-10 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0017_alter_shoppingcart_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Src.product'),
        ),
    ]