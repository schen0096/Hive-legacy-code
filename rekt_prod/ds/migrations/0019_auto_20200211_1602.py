# Generated by Django 2.1.5 on 2020-02-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0018_auto_20200210_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='blizz_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='discord_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='epic_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='playstation_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='steam_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='switch_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
