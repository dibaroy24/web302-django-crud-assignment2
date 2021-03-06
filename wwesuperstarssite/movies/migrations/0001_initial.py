# Generated by Django 2.1.3 on 2018-12-15 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wwesuperstars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track', models.FileField(upload_to='movies/songs/2018/12/14/')),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='poster', serialize=False, to='movies.Movie')),
                ('image', models.ImageField(upload_to='movies/posters/2018/12/14/')),
            ],
        ),
        migrations.AddField(
            model_name='themesong',
            name='movie',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='wwesuperstars',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='wwesuperstars.WWESuperstar'),
        ),
    ]
