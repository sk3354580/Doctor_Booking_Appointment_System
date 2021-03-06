# Generated by Django 4.0.4 on 2022-05-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('is_veg', models.BooleanField(default=True)),
            ],
        ),
    ]
