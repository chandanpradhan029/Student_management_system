# Generated by Django 3.1.6 on 2021-02-26 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210226_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='dob',
        ),
    ]
