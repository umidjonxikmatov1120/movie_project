# Generated by Django 5.0.6 on 2024-07-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
            },
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'register',
                'verbose_name_plural': 'registers',
            },
        ),
    ]
