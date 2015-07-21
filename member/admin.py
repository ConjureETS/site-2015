from django.contrib import admin
from member import models, forms

@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    form = forms.MemberAdminForm
    fields = ['first_name', 'last_name', 'email', 'photo', 'is_admin', 'position']
    list_display = ['first_name', 'last_name', 'is_admin']
