from django.contrib import admin

from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

admin.site.register(Room, RoomAdmin)
