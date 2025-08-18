from modeltranslation.translator import register, TranslationOptions
from .models import Starter

@register(Starter)
class StarterTranslationOptions(TranslationOptions):
    fields = ( "content", ) 