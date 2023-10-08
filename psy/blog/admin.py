from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'psychologist','topic', 'title', 'is_published', 'get_html_photo', 'created_at')  # колонки, які відображаються в списку адмінки
    list_filter = ('topic',)  # сортування по колонці
    search_fields = ('topic__title', 'title')  # пошук по колонках
    list_editable = ('topic', 'is_published', 'psychologist')  # дозвіл на редагування поля відразу зі списку в адмінці
    prepopulated_fields = {'slug': ('title',)}

    def get_html_photo(self, object):
        if object.profile_picture:
            return mark_safe(f"<img src='{object.profile_picture.url}' width=50>")

    get_html_photo.short_description = 'Зображення'
    def save_model(self, request, obj, form, change):
        # Перед збереженням поста, автором буде поточний користувач
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_exclude(self, request, obj=None):
        # При редагуванні поста, поле "author" все одно не буде відображатись
        if obj is not None:
            return super().get_exclude(request, obj)
        return self.exclude


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
