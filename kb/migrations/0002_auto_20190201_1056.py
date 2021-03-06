# Generated by Django 2.1.5 on 2019-02-01 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer', models.TextField(max_length=4000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('faq_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='kb_category',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='kb_answer',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='kb_answer',
            name='faq',
        ),
        migrations.RemoveField(
            model_name='kb_faq',
            name='starter',
        ),
        migrations.RemoveField(
            model_name='kb_faq',
            name='tag_faq',
        ),
        migrations.RenameModel(
            old_name='kb_tag',
            new_name='tag',
        ),
        migrations.DeleteModel(
            name='kb_answer',
        ),
        migrations.DeleteModel(
            name='kb_faq',
        ),
        migrations.AddField(
            model_name='faq',
            name='tag_faq',
            field=models.ManyToManyField(to='kb.tag'),
        ),
        migrations.AddField(
            model_name='answer',
            name='faq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='kb.faq'),
        ),
    ]
