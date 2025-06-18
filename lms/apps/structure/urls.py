from django.urls import path

from .views import *

app_name = 'structure'

urlpatterns = [
    path('academic-year/', academic_year_list, name='academic_year_list'),
    path('academic-year/create/', academic_year_create, name='academic_year_create'),
    path('academic-year/<int:pk>/delete/', academic_year_delete, name='academic_year_delete'),
    path('academic-year/<int:id>/detail/', academic_year_detail, name='academic_year_detail'),
    path('academic-year/<int:id>/update/', academic_year_update, name='academic_year_update'),
    
    path('kafedra/', kafedra_list, name='kafedra_list'),
    path('kafedra/create/', kafedra_create, name='kafedra_create'),
    path('kafedra/<int:pk>/delete/', kafedra_delete, name='kafedra_delete'),
    path('kafedra/<int:id>/detail/', kafedra_detail, name='kafedra_detail'),
    path('kafedra/<int:id>/update/', kafedra_update, name='kafedra_update'),
    
    path('lesson-time/', lesson_time_list, name='lesson_time_list'),
    path('lesson-time/create/', lesson_time_create, name='lesson_time_create'),
    path('lesson-time/<int:pk>/delete/', lesson_time_delete, name='lesson_time_delete'),
    path('lesson-time/<int:id>/detail/', lesson_time_detail, name='lesson_time_detail'),
    path('lesson-time/<int:id>/update/', lesson_time_update, name='lesson_time_update'),
    
    path('science/', science_list, name='science_list'),
    path('science/create/', science_create, name='science_create'),
    path('science/<int:pk>/delete/', science_delete, name='science_delete'),
    path('science/<int:id>/detail/', science_detail, name='science_detail'),
    path('science/<int:id>/update/', science_update, name='science_update'),
    
    path('student-group/', student_group_list, name='student_group_list'),
    path('student-group/create/', student_group_create, name='student_group_create'),
    path('student-group/<int:pk>/delete/', student_group_delete, name='student_group_delete'),
    path('student-group/<int:id>/detail/', student_group_detail, name='student_group_detail'),
    path('student-group/<int:id>/update/', student_group_update, name='student_group_update'),
    path('student-group/<int:pk>/reject/user/<int:user_id>/', student_group_reject_student, name='student_group_reject_student'),
    
    path('science-group/', science_group_list, name='science_group_list'),
    path('science-group/create/', science_group_create, name='science_group_create'),
    path('science-group/<int:pk>/delete/', science_group_delete, name='science_group_delete'),
    path('science-group/<int:id>/detail/', science_group_detail, name='science_group_detail'),
    path('science-group/<int:id>/update/', science_group_update, name='science_group_update'),
]