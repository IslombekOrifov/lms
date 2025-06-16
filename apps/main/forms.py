from django import forms

from ckeditor.widgets import CKEditorWidget

from account.models import RoleName
from .models import School, Module, Lesson, NB


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = ['created_at', 'updated_at',]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'Enter school address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email address'}),
        }


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'description', 'order',]


class LessonForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lesson
        fields = ['name', 'lesson_date', 'about', 'text', 'is_active']


class NBForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.lesson = kwargs.pop('lesson')
        super().__init__(*args, **kwargs)
        
        students = self.lesson.module.group.group.students.filter(
            role__name=RoleName.STUDENT
        ).order_by('last_name', 'first_name')
        
        for student in students:
            self.fields[f'student_{student.id}'] = forms.BooleanField(
                required=False,
                label=f"{student.last_name} {student.first_name}",
                initial=True
            )