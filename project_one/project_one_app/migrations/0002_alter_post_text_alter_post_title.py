# Generated by Django 5.0.6 on 2024-06-02 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_one_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
