# Generated by Django 3.1.6 on 2021-02-24 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_student_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
    ]
