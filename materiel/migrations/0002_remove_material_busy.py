# Generated by Django 3.2.9 on 2021-12-26 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='Busy',
        ),
    ]
