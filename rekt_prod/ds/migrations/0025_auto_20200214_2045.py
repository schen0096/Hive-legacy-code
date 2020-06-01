# Generated by Django 2.1.5 on 2020-02-14 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ds', '0024_auto_20200212_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_photo',
            name='updated_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='UpdatedPhotos', to=settings.AUTH_USER_MODEL),
        ),
    ]
