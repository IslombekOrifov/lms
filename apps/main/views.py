from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone

from .models import School, Lesson, Module, NB, NBandRating
from .forms import SchoolForm, ModuleForm, LessonForm, NBForm

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


@login_required
@teacher_required
def teacher_module_create(request, group_id):
    group = ScienceGroup.objects.get(id=group_id)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.group = group
            module.save()
            return redirect(reverse_lazy('main:teacher_group_detail', args=[group_id]))
    else:
        form = ModuleForm()
    return render(request, 'main/module-update.html', {'form': form, 'group': group})


@login_required
@teacher_required
def teacher_lesson_create(request, module_id):
    module = Module.objects.get(id=module_id)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.module = module
            lesson.save()
            return redirect(reverse_lazy('main:teacher_group_detail', args=[module.group.id]))
    else:
        form = LessonForm()
    return render(request, 'main/lesson-update.html', {'form': form,})


@login_required
@teacher_required
def teacher_lesson_update(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            return redirect(reverse_lazy('main:teacher_lesson_detail', args=[lesson.id]))
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'main/lesson-update.html', {'form': form,})


@login_required
@teacher_required
def nb_create(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    
    if request.method == 'POST':
        form = NBForm(request.POST, lesson=lesson)
        if form.is_valid():
            for field_name, is_not_present in form.cleaned_data.items():
                if is_not_present and field_name.startswith('student_'):
                    student_id = int(field_name.split('_')[1])
                    NB.objects.create(
                        student_id=student_id,
                        lesson=lesson,
                        cause_status=False,
                    )
            
            NBandRating.objects.create(lesson=lesson, is_checked=True)
            return redirect('main:lesson_detail', id=lesson.id)
    else:
        nb_and_rating = NBandRating.objects.filter(lesson=lesson, is_checked=True, created_at__date=timezone.now().date()).exists()
        if not nb_and_rating:
            form = NBForm(request.POST, lesson=lesson)
        else:
            raise PermissionDenied
    
    return render(request, 'main/nb-create.html', {
        'lesson': lesson,
        'form': form
    })


@login_required
@teacher_required
def lesson_detail(request, id):
    lesson = Lesson.objects.get(id=id)
    rated = False
    checked = False
    nb_and_rating = NBandRating.objects.filter(lesson=lesson, created_at__date=timezone.now().date()).first()
    if nb_and_rating:
        rated = nb_and_rating.is_rated
        checked = nb_and_rating.is_checked
    context = {
        'lesson': lesson,
        'rated': rated,
        'checked': checked
    }
    return render(request, 'main/lesson-detail.html', context)



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