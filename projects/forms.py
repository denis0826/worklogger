from django import forms

from .models import Project


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class LogForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    remarks = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'class': 'form-control'}))