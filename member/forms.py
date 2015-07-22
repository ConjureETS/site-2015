from django import forms
from member import models

class MemberAdminForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = ['first_name', 'last_name', 'email', 'photo', 'is_admin', 'position']
