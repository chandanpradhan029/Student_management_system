# Generated by Django 3.1.6 on 2021-02-22 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210222_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='female',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='student',
            name='male',
        ),
    ]
