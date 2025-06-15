from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import (
    School, Task, Submission, Lesson, LessonSource, 
    NB, RatingNotebook, Module
)


admin.site.site_header = "LMS Administration"
admin.site.site_title = "LMS Admin Portal"
admin.site.index_title = "Welcome to LMS Admin"


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')


class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 0
    raw_id_fields = ('student',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'deadline')
    list_filter = ('group',)
    inlines = [SubmissionInline]
    date_hierarchy = 'deadline'


class LessonSourceInline(admin.TabularInline):
    model = LessonSource
    extra = 1


class LessonAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lesson
        fields = '__all__'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'lesson_date', 'status')
    list_filter = ('status', 'module')
    inlines = [LessonSourceInline]
    date_hierarchy = 'lesson_date'
    form = LessonAdminForm


@admin.register(RatingNotebook)
class RatingNotebookAdmin(admin.ModelAdmin):
    list_display = ('student', 'science_name', 'grade')
    raw_id_fields = ('student', 'science_name')
    search_fields = ('student__username',)
    
    
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('group', 'title', 'order')
    raw_id_fields = ('group',)
    search_fields = ('title', 'group')