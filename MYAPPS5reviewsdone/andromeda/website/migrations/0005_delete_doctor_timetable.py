# Generated by Django 4.0.5 on 2022-06-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rating_doctor_schedule_doctor_reply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='doctor_timetable',
        ),
    ]
