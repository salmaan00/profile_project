# Generated by Django 5.0.6 on 2024-06-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='certifications',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='project_showcases',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_experience',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]