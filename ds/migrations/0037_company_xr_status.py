# Generated by Django 2.1.5 on 2020-03-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0036_auto_20200310_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='xr_status',
            field=models.CharField(default='INACTIVE', max_length=30),
        ),
    ]
