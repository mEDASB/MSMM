# Generated by Django 4.0.2 on 2022-02-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ste', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='societe',
            name='is_completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
