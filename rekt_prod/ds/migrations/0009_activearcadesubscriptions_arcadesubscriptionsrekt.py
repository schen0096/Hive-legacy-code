# Generated by Django 2.1.5 on 2020-01-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0008_auto_20191023_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveArcadeSubscriptions',
            fields=[
                ('subscription_id', models.CharField(blank=True, max_length=12, primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('ftp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'active_arcade_subscriptions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArcadeSubscriptionsRekt',
            fields=[
                ('subscription_id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('subscription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'arcade_subscriptions_rekt',
                'managed': False,
            },
        ),
    ]
