# Generated by Django 4.2.10 on 2024-02-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_alter_search_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='categories',
            field=models.JSONField(default=list, null=True, verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_type',
            field=models.CharField(max_length=300, null=True, verbose_name='group type'),
        ),
        migrations.AlterField(
            model_name='group',
            name='location',
            field=models.CharField(max_length=150, null=True, verbose_name='location'),
        ),
        migrations.AlterField(
            model_name='group',
            name='rules',
            field=models.TextField(null=True, verbose_name='rules'),
        ),
        migrations.AlterField(
            model_name='group',
            name='tags',
            field=models.JSONField(default=list, null=True, verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='group',
            name='website',
            field=models.URLField(null=True, verbose_name='website'),
        ),
    ]
