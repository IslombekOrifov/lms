from django.urls import path

from .views import *

app_name = 'main'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('director/', director_dashboard, name='director_dashboard'),
    
    path('school/detail/', school_detail, name='school_detail'),
    
    path('teacher/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher/groups/', teacher_group, name='teacher_group'),
    path('teacher/groups/detail<int:id>/', teacher_group_detail, name='teacher_group_detail'),
    
    path('module/create/<int:group_id>/', teacher_module_create, name='teacher_module_create'),
    
    path('lesson/detail/<int:id>/', lesson_detail, name="lesson_detail"),
    path('lesson/create/<int:module_id>/', teacher_lesson_create, name='teacher_lesson_create'),
    path('lesson/update/<int:lesson_id>/', teacher_lesson_update, name='teacher_lesson_update'),
    
    path('nb/create/<int:lesson_id>/', nb_create, name='nb_create'),
]