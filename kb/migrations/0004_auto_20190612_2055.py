# Generated by Django 2.1.5 on 2019-06-12 20:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kb', '0003_faq_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq_log',
            fields=[
                ('faq_logging_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('answer', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_log', to='kb.category')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='faq_log_id',
            fields=[
                ('faq_log_id', models.AutoField(primary_key=True, serialize=False)),
                ('faq_id_value', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq_log',
            name='faq_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_log', to='kb.faq_log_id'),
        ),
    ]
