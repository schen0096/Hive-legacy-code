# Generated by Django 2.1.5 on 2019-07-09 18:53

from django.db import migrations, models
import kb.models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0004_auto_20190612_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='pin_value',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='faq_log',
            name='last_updated',
            field=models.DateTimeField(default=kb.models.est),
        ),
    ]
