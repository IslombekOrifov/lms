from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.views import LoginView

from .models import CustomUser
from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'account/login.html'
    
    def get_success_url(self):
        return self.request.GET.get('next', '/main/')


def users_list(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'account/users-list.html', context)

def users_add(request):
    users = CustomUser.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'account/add-user.html', context)


def user_detail(request, id):
    user = CustomUser.objects.get(pk=id)
    context = {
        'user': user,
    }
    return render(request, 'account/view-profile.html', context)

def user_update(request, id):
    user = CustomUser.objects.get(pk=id)
    context = {
        'user': user,
    }
    return render(request, 'account/view-profile.html', context)

def user_delete(request, id):
    user = CustomUser.objects.get(pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('account:users_list')   
    raise Http404("User not found")