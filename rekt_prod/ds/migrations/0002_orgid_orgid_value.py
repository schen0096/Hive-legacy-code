# Generated by Django 2.1.5 on 2019-02-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgid',
            name='orgid_value',
            field=models.CharField(default='DEFAULT VALUE', max_length=50, unique=True),
        ),
    ]
