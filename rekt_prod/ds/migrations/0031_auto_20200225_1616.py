# Generated by Django 2.1.5 on 2020-02-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0030_auto_20200224_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='arcade_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company_log',
            name='arcade_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
