from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from embed_video.admin import AdminVideoMixin

from .models import *

class InfoAdmin(TranslationAdmin):
    pass

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Info, InfoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(ContactInfo)