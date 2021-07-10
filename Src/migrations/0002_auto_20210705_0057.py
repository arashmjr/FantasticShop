# Generated by Django 3.2.4 on 2021-07-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('gender', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='UserDomainModel',
        ),
    ]