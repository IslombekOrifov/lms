from django.urls import path

from .views import dashboard, school_detail

app_name = 'main'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('school/detail/', school_detail, name='school_detail'),
]