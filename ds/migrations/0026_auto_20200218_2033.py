# Generated by Django 2.1.5 on 2020-02-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0025_auto_20200214_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitch_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]