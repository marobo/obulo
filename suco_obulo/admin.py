from django.contrib import admin
from .models import Post, Page


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'author')
    fieldsets = [
        (None, {'fields': [('title', 'overview', 'image', 'page')]}),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Page)
