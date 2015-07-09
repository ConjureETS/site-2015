from django.contrib import admin
from project import models, forms


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    form = forms.ProjectAdminForm
    fields = ['name', 'description', 'download', 'screenshot', 'members']
    list_display = ['name']
