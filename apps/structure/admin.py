from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from mptt.admin import DraggableMPTTAdmin
from .models import (
    AcademicYear, Kafedra, LessonTime, Science, 
    StudentGroup, ScienceGroup, ScheduleTable
)

class ActiveFilter(SimpleListFilter):
    title = 'Active status'
    parameter_name = 'is_active'

    def lookups(self, request, model_admin):
        return (('yes', 'Active'), ('no', 'Inactive'))

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_active=True)
        if self.value() == 'no':
            return queryset.filter(is_active=False)


@admin.register(AcademicYear)
class AcademicYearAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'season', 'start_date', 'end_date', 'is_active')
    list_filter = (ActiveFilter, 'season')
    search_fields = ('name',)


@admin.register(LessonTime)
class LessonTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'is_active', 'school')
    list_filter = (ActiveFilter,)
    search_fields = ('name',)


@admin.register(Science)
class ScienceAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name', 'code', 'school', 'academic_year')
    list_filter = (ActiveFilter, 'academic_year')
    search_fields = ('name', 'code')


@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'school', 'is_active')
    list_filter = (ActiveFilter, 'school')
    search_fields = ('name', 'code')
    raw_id_fields = ('department_user', 'school')


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'lang', 'school', 'tyutor')
    list_filter = ('lang', 'school')
    raw_id_fields = ('tyutor', 'students')
    filter_horizontal = ('students',)


@admin.register(ScheduleTable)
class ScheduleTableAdmin(admin.ModelAdmin):
    list_display = ('week_day', 'lesson_time', 'teacher', 'group')
    raw_id_fields = ('teacher', 'group', 'lesson_time')


@admin.register(ScienceGroup)
class ScienceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'science', 'group', 'teacher')
    list_filter = (ActiveFilter, 'science')
    search_fields = ('name', 'code')
    
