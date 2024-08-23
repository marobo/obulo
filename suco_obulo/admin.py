from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Page


class PoageAdmin(TranslationAdmin):
    list_display = ('name',)
    fieldsets = [
        (None, {'fields': [('name',)]}),
    ]


class PostAdmin(SummernoteModelAdmin, TranslationAdmin):
    summernote_fields = ('overview',)
    list_display = ('title', 'page', 'author',)
    fieldsets = [
        (None, {'fields': [('title', 'overview', 'image', 'page',)]}),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Page, PoageAdmin)
