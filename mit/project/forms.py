from django import forms
from project.models import Project


class ProjectForm(forms.ModelForm):
    time = forms.DateField(label='開始日期')
    title = forms.CharField(label='計畫主題',max_length=128)
    company = forms.CharField(label='合作廠商',max_length=128)
    
    class Meta:
         model = Project
         fields = ('time', 'title', 'company')