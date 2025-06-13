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
]