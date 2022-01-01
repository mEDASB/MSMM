# Generated by Django 3.2.9 on 2021-12-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='CIN',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='cp_CIN',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='me',
            name='domaine',
            field=models.CharField(choices=[('in progress', 'in progress'), ('out the order', 'out the order'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='full_Name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='phone',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='ville',
            field=models.CharField(choices=[('in progress', 'in progress'), ('out the order', 'out the order'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]
