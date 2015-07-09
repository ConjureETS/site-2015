from django.contrib import admin
from member import models

@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'photo']
    list_display = ['first_name', 'last_name']
