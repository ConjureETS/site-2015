from django import forms
from member import models

class MemberAdminForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    class Meta:
        model = models.Member
