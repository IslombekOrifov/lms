from django.urls import path

from .views import index

app_name = 'structure'

urlpatterns = [
    path('', index, name='index'),
]