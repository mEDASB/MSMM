# Generated by Django 3.2.9 on 2022-01-22 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materiel', '0002_remove_material_busy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='me',
        ),
        migrations.RemoveField(
            model_name='material',
            name='ste',
        ),
        migrations.AddField(
            model_name='material',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]