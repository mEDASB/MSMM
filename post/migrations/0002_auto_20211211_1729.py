# Generated by Django 3.2.9 on 2021-12-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mepost',
            old_name='user',
            new_name='me',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='me',
        ),
        migrations.AddField(
            model_name='post',
            name='date_experation',
            field=models.DateField(null=True),
        ),
    ]