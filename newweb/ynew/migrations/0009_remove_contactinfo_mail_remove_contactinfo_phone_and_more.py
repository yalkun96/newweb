# Generated by Django 4.2.4 on 2023-12-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ynew', '0008_alter_contactinfo_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='phone',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='contact',
            field=models.CharField(max_length=50, null=True, verbose_name='contact'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='whatsapp',
            field=models.TextField(max_length=50, verbose_name='contact_info'),
        ),
    ]