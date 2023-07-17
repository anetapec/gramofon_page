from django.contrib import admin
from .models import Local, ShortDescribe, Room


@admin.register(Local)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title' ]

admin.site.register(Room)
admin.site.register(ShortDescribe)






