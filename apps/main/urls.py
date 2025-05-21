from django.urls import path

from .views import dashboard

app_name = 'main'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]