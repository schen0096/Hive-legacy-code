# Generated by Django 2.1.5 on 2020-02-10 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0013_profile_photo_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_photo',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserPhoto', to=settings.AUTH_USER_MODEL),
        ),
    ]
