# Generated by Django 2.1.3 on 2018-12-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20181219_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='role',
        ),
        migrations.AddField(
            model_name='poster',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
