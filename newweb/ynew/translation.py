from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('title', 'info',)

@register(Video)
class InfoTranslationOptions(TranslationOptions):
    pass