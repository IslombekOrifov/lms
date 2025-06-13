from django import forms

from .models import School


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = ['created_at', 'updated_at',]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter school address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
        }