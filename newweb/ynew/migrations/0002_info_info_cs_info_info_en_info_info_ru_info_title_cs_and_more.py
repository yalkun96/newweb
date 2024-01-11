# Generated by Django 4.2.4 on 2023-10-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ynew', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='info_cs',
            field=models.TextField(blank=True, null=True, verbose_name='info'),
        ),
        migrations.AddField(
            model_name='info',
            name='info_en',
            field=models.TextField(blank=True, null=True, verbose_name='info'),
        ),
        migrations.AddField(
            model_name='info',
            name='info_ru',
            field=models.TextField(blank=True, null=True, verbose_name='info'),
        ),
        migrations.AddField(
            model_name='info',
            name='title_cs',
            field=models.CharField(max_length=300, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='info',
            name='title_en',
            field=models.CharField(max_length=300, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='info',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='title'),
        ),
    ]