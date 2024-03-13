from django.contrib import admin

from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'preview_image')  # Отображение превью изображения в списке мероприятий
    search_fields = ('title', 'description')  # Поля для поиска
    list_filter = ('date',)  # Фильтрация по дате