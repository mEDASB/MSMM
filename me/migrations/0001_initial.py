# Generated by Django 3.2.9 on 2021-12-11 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=14)),
                ('ville', models.CharField(choices=[('in progress', 'in progress'), ('out the order', 'out the order'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('full_Name', models.CharField(max_length=50)),
                ('CIN', models.CharField(max_length=10)),
                ('cp_CIN', models.ImageField(upload_to='')),
                ('Busy', models.BooleanField(default=False, null=True)),
                ('active', models.BooleanField()),
                ('domaine', models.CharField(choices=[('in progress', 'in progress'), ('out the order', 'out the order'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], max_length=100)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
