from django.contrib import admin
from .models import Local, Room, ShortDescribe


@admin.register(Local)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title' ]

admin.site.register(Room)
admin.site.register(ShortDescribe)

class NoteRomm(admin.TabularInline):
    model = Room
    verbose_name_plural = "Room"

class DepartmentAdmin(admin.ModelAdmin):
    inlines= [NoteRomm]