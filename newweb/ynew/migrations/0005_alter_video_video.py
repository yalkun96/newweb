# Generated by Django 4.2.4 on 2023-11-29 22:59

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ynew', '0004_video_uploaded_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
