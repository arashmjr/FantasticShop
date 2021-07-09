# Generated by Django 3.2.4 on 2021-07-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0013_alter_user_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.BigIntegerField()),
                ('category_id', models.BigIntegerField()),
                ('name', models.CharField(max_length=40)),
                ('thumbnail', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='JunkDomainModel',
        ),
    ]
