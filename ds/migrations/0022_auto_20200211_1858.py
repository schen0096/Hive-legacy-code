# Generated by Django 2.1.5 on 2020-02-11 18:58

from django.db import migrations, models
import rekt.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0021_auto_20200211_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_photo',
            name='upload_photo',
            field=models.FileField(storage=rekt.storage_backends.photo_storage(), upload_to=''),
        ),
    ]
