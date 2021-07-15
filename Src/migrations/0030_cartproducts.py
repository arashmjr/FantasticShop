# Generated by Django 3.2.4 on 2021-07-15 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0029_auto_20210714_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProducts',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('quantity', models.BigIntegerField()),
                ('order_status', models.IntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Src.carts')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Src.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Src.user')),
            ],
        ),
    ]