# Generated by Django 5.1.5 on 2025-03-24 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectname', '0007_alter_question_creator'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='creator',
        ),
        migrations.AddField(
            model_name='quiz',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions_created', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
