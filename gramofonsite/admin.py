from django.contrib import admin
from .models import Local

admin.site.register(Local)

class TopicAdmin(admin.ModelAdmin):
    list_display = ['Title']