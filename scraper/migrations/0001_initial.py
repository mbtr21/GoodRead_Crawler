# Generated by Django 4.2.10 on 2024-02-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('rate', models.CharField(max_length=10, verbose_name='rate')),
                ('numbers_of_ratings', models.IntegerField()),
                ('numbers_of_reviews', models.IntegerField()),
                ('genres', models.JSONField(default=list, verbose_name='genres')),
                ('pages_format', models.CharField(max_length=100, verbose_name='pages format')),
                ('publication_info', models.TextField(verbose_name='publication_info')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('tags', models.JSONField(default=list, verbose_name='tags')),
                ('rules', models.TextField(verbose_name='rules')),
                ('categories', models.JSONField(default=list, verbose_name='categories')),
                ('website', models.URLField(verbose_name='website')),
                ('location', models.CharField(max_length=150, verbose_name='location')),
                ('group_type', models.CharField(max_length=300, verbose_name='group type')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]