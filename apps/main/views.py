from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import School
from .forms import SchoolForm


def dashboard(request):
    """
    Render the dashboard page.
    """
    return render(request, 'main/index.html')

# def teacher_required(view_func):
#     """Декоратор для проверки роли учителя"""
#     def wrapper(request, *args, **kwargs):
#         if not request.user.role == 'teacher':
#             raise PermissionDenied
#         return view_func(request, *args, **kwargs)
#     return wrapper

# @login_required
# @teacher_required
# def teacher_dashboard(request):
#     # context = {'role_specific_data': get_teacher_data()}
#     return render(request, 'dashboard.html')


def school_detail(request):
    user = request.user
    school = user.school
    if school and user.role.name == 'director':
        print('keldi')
        if request.method == 'POST':
            form = SchoolForm(request.POST, instance=school)
            if form.is_valid():
                form.save()
                return redirect('main:school_detail')
        else:
            form = SchoolForm(instance=school)
        return render(request, 'main/company.html', {'form': form})
    else:
        raise Http404()