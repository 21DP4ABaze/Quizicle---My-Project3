# Generated by Django 5.1.5 on 2025-03-13 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectname', '0004_rename_questioncount_quiz_question_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='AdditionalImage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='PointsForQuestion',
            new_name='points_for_question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Quiz',
            new_name='quiz',
        ),
    ]
