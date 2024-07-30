from modeltranslation.translator import translator, TranslationOptions
from suco_obulo.models import Page, Post


class PageTranslationOptions(TranslationOptions):
    fields = ('name',)


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'overview',)


translator.register(Page, PageTranslationOptions)
translator.register(Post, PostTranslationOptions)
