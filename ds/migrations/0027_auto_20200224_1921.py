# Generated by Django 2.1.5 on 2020-02-24 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0026_auto_20200218_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='company',
            name='arcade_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_lable',
            field=models.ManyToManyField(blank=True, to='ds.label'),
        ),
        migrations.AlterField(
            model_name='company',
            name='poc_email',
            field=models.EmailField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='company',
            name='poc_firstname',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='poc_lastname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
