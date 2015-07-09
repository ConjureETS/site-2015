from django.contrib import admin
from blog import models, forms


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    form = forms.ArticleAdminForm
    fields = ['title', 'author', 'text', 'photo']
    list_display = ['title', 'author']
