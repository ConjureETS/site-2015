from django import forms
from member import models as member_models


class MemberMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + ' ' + obj.last_name



class ProjectAdminForm(forms.ModelForm):
    members = MemberMultipleChoiceField(queryset=member_models.Member.objects.all())
