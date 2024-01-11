from django.db import models
from django.urls import reverse
from embed_video.fields import EmbedVideoField


class Info(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    slug = models.SlugField(unique=True, verbose_name='URL')
    info = models.TextField(blank=True, verbose_name='info')

    def __str__(self):
        return self.info

    #def get_absolute_url(self):
        #return reverse('post', kwargs={'post_slug': self.slug})


class ContactInfo(models.Model):
    contact = models.CharField(max_length=50, verbose_name='contact', null=True)
    contact_info = models.TextField(max_length=50, verbose_name='contact_info', null=True)

    def __str__(self):
        return self.contact_info


class Video(models.Model):
    name = models.CharField(max_length=200, null=True)
    video = EmbedVideoField(null=True, blank=True)
    uploaded_video = models.FileField(upload_to='video/%y', null=True, blank=True)
