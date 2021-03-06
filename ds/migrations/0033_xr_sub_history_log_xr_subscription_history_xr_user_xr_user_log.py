# Generated by Django 2.1.5 on 2020-03-03 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ds.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ds', '0032_auto_20200226_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='xr_sub_history_log',
            fields=[
                ('xr_sub_id_log', models.AutoField(primary_key=True, serialize=False)),
                ('xr_sub_id', models.IntegerField()),
                ('subscription_start', models.DateField()),
                ('subscription_end', models.DateField()),
                ('xr_tier', models.CharField(max_length=20)),
                ('time', models.DateTimeField(default=ds.models.est)),
                ('log_notes', models.CharField(max_length=100)),
                ('orgid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_sub_his_log', to='ds.orgid')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_sub_his_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='xr_subscription_history',
            fields=[
                ('xr_sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('xr_subscription_start', models.DateField()),
                ('xr_subscription_end', models.DateField()),
                ('xr_tier', models.CharField(max_length=20)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_sub_history', to='ds.company')),
            ],
            options={
                'verbose_name_plural': 'xr_subscription_histories',
            },
        ),
        migrations.CreateModel(
            name='xr_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('xr_user_id', models.CharField(max_length=30)),
                ('xr_user_firstname', models.CharField(max_length=30)),
                ('xr_user_lastname', models.CharField(max_length=30)),
                ('xr_user_email', models.CharField(max_length=250)),
                ('comopany_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_user', to='ds.company')),
            ],
        ),
        migrations.CreateModel(
            name='xr_user_log',
            fields=[
                ('xr_user_log_id', models.AutoField(primary_key=True, serialize=False)),
                ('xr_user_id', models.CharField(max_length=30)),
                ('xr_user_firstname', models.CharField(max_length=30)),
                ('xr_user_lastname', models.CharField(max_length=30)),
                ('xr_user_email', models.EmailField(max_length=250)),
                ('xr_user_status', models.CharField(max_length=15)),
                ('time', models.DateTimeField(default=ds.models.est)),
                ('log_notes', models.CharField(max_length=100)),
                ('orgid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_user_log', to='ds.orgid')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xr_user_editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
