from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Friend)
admin.site.register(ChatMessage)
