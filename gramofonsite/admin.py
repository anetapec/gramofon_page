from django.contrib import admin
from .models import Local


@admin.register(Local)
class TopicAdmin(admin.ModelAdmin):
   list_display = ['title_local' ]

#admin.site.register(Local)
# admin.site.register(ShortDescribe)





