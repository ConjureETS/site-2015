from django import forms
from ckeditor import widgets
from blog import models


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget=widgets.CKEditorWidget())
    class Meta:
        model = models.Article
        fields = ['title', 'author', 'text', 'photo']