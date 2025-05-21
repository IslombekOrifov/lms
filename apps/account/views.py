from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return self.request.GET.get('next', '/dashboard/')