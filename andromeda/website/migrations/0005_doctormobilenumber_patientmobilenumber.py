# Generated by Django 4.0.4 on 2022-05-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_doctormobilenumber_delete_patientmobilenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctormobilenumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('doctormobilenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='patientmobilenumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=50)),
                ('patientmobilenumber', models.IntegerField()),
            ],
        ),
    ]