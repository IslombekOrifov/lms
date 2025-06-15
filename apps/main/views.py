from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import School
from .forms import SchoolForm

from structure.models import ScienceGroup


def teacher_required(view_func):
    """Декоратор для проверки роли учителя"""
    def wrapper(request, *args, **kwargs):
        if not request.user.role.name == 'teacher':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

def dashboard(request):
    """
    Render the dashboard page.
    """
    if request.user.role.name == 'teacher':
        redirect_url = 'main:teacher_dashboard'
    else:
        redirect_url = 'main:director_dashboard'
    return redirect(redirect_url)

def director_dashboard(request):
    # context = {'role_specific_data': get_teacher_data()}
    return render(request, 'main/index.html')



@login_required
@teacher_required
def teacher_dashboard(request):
    # context = {'role_specific_data': get_teacher_data()}
    return render(request, 'main/index_teacher.html')


@login_required
@teacher_required
def teacher_group(request):
    groups = ScienceGroup.objects.filter(teacher=request.user, is_active=True)
    context = {'groups': groups}
    return render(request, 'main/teacher-group.html', context)


@login_required
@teacher_required
def teacher_group_detail(request, id):
    group = ScienceGroup.objects.filter(pk=id, teacher=request.user, is_active=True).prefetch_related('modules', 'modules__lesson_to_group_model').first()
    context = {'group': group}
    return render(request, 'main/module.html', context)



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