from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

from .models import *
from .forms import *


def academic_year_list(request):
    academic_years = AcademicYear.objects.all()
    context = {
        'academic_years': academic_years
    }
    return render(request, 'structure/academic-year.html', context)

def academic_year_delete(request, pk):
    if request.method == 'POST':
        academic_year = AcademicYear.objects.get(id=pk)
        academic_year.delete()
        return redirect('structure:academic_year_list')
    else:
        return Http404()

def academic_year_detail(request, id):
    academic_year = AcademicYear.objects.get(pk=id)
    context = {
        'academic_year': academic_year
    }
    return render(request, 'structure/academ-detail.html', context)

def academic_year_update(request, id):
    academic_year = AcademicYear.objects.get(pk=id)
    if request.method == 'POST':
        form = AcademicYearForm(request.POST, instance=academic_year)
        if form.is_valid():
            form.save()
            return redirect('structure:academic_year_list')
    else:
        form = AcademicYearForm(instance=academic_year)
    return render(request, 'structure/academ-update.html', {'form': form})

def academic_year_create(request):
    if request.method == 'POST':
        form = AcademicYearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('structure:academic_year_list')
    else:
        form = AcademicYearForm()
    return render(request, 'structure/academ-update.html', {'form': form})



def kafedra_list(request):
    kafedras = Kafedra.objects.all()
    context = {
        'kafedras': kafedras
    }
    return render(request, 'structure/kafedra.html', context)

def kafedra_delete(request, pk):
    if request.method == 'POST':
        kafedra = Kafedra.objects.get(id=pk)
        kafedra.delete()
        return redirect('structure:kafedra_list')
    else:
        return Http404()

def kafedra_detail(request, id):
    kafedra = Kafedra.objects.get(pk=id)
    context = {
        'kafedra': kafedra
    }
    return render(request, 'structure/kafedra-detail.html', context)

def kafedra_update(request, id):
    kafedra = Kafedra.objects.get(pk=id)
    if request.method == 'POST':
        form = KafedraForm(request.POST, instance=kafedra, request=request)
        if form.is_valid():
            form.save()
            return redirect('structure:kafedra_list')
    else:
        form = KafedraForm(instance=kafedra, request=request)
    return render(request, 'structure/kafedra-update.html', {'form': form})

def kafedra_create(request):
    if request.method == 'POST':
        form = KafedraForm(request.POST, request=request)
        if form.is_valid():
            kafedra = form.save(commit=False)
            kafedra.school = request.user.school
            kafedra.save()
            return redirect('structure:kafedra_list')
    else:
        form = KafedraForm(request=request)
    return render(request, 'structure/kafedra-update.html', {'form': form})



def lesson_time_list(request):
    lesson_times = LessonTime.objects.all()
    context = {
        'lesson_times': lesson_times
    }
    return render(request, 'structure/lesson-time.html', context)

def lesson_time_delete(request, pk):
    if request.method == 'POST':
        lesson_time = LessonTime.objects.get(id=pk)
        lesson_time.delete()
        return redirect('structure:lesson_time_list')
    else:
        return Http404()

def lesson_time_detail(request, id):
    lesson_time = LessonTime.objects.get(pk=id)
    context = {
        'lesson_time': lesson_time
    }
    return render(request, 'structure/lesson-time-detail.html', context)

def lesson_time_update(request, id):
    lesson_time = LessonTime.objects.get(pk=id)
    if request.method == 'POST':
        form = LessonTimeForm(request.POST, instance=lesson_time, request=request)
        if form.is_valid():
            form.save()
            return redirect('structure:lesson_time_list')
    else:
        form = LessonTimeForm(instance=lesson_time)
    return render(request, 'structure/lesson-time-update.html', {'form': form})

def lesson_time_create(request):
    if request.method == 'POST':
        form = LessonTimeForm(request.POST)
        if form.is_valid():
            lesson_time = form.save(commit=False)
            lesson_time.school = request.user.school
            lesson_time.save()
            return redirect('structure:lesson_time_list')
    else:
        form = LessonTimeForm()
    return render(request, 'structure/lesson-time-update.html', {'form': form})




def science_list(request):
    sciences = Science.objects.all()
    context = {
        'sciences': sciences
    }
    return render(request, 'structure/science.html', context)

def science_delete(request, pk):
    if request.method == 'POST':
        science = Science.objects.get(id=pk)
        science.delete()
        return redirect('structure:science_list')
    else:
        return Http404()

def science_detail(request, id):
    science = Science.objects.get(pk=id)
    context = {
        'science': science
    }
    return render(request, 'structure/science-detail.html', context)

def science_update(request, id):
    science = Science.objects.get(pk=id)
    if request.method == 'POST':
        form = ScienceForm(request.POST, instance=science, request=request)
        if form.is_valid():
            form.save()
            return redirect('structure:science_list')
    else:
        form = ScienceForm(instance=science)
    return render(request, 'structure/science-update.html', {'form': form})

def science_create(request):
    if request.method == 'POST':
        form = ScienceForm(request.POST)
        if form.is_valid():
            science = form.save(commit=False)
            science.school = request.user.school
            science.save()
            return redirect('structure:science_list')
    else:
        form = ScienceForm()
    return render(request, 'structure/science-update.html', {'form': form})




def student_group_list(request):
    student_groups = StudentGroup.objects.all()
    context = {
        'student_groups': student_groups
    }
    return render(request, 'structure/student-group.html', context)

def student_group_delete(request, pk):
    if request.method == 'POST':
        student_group = StudentGroup.objects.get(id=pk)
        student_group.delete()
        return redirect('structure:student_group_list')
    else:
        return Http404()

def student_group_detail(request, id):
    student_group = StudentGroup.objects.get(pk=id)
    context = {
        'student_group': student_group
    }
    return render(request, 'structure/student-group-detail.html', context)

def student_group_update(request, id):
    student_group = StudentGroup.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentGroupForm(request.POST, instance=student_group, request=request)
        if form.is_valid():
            form.save()
            return redirect('structure:student_group_list')
    else:
        form = StudentGroupForm(instance=student_group, request=request)
    return render(request, 'structure/student-group-update.html', {'form': form})

def student_group_create(request):
    if request.method == 'POST':
        form = StudentGroupForm(request.POST, request=request)
        if form.is_valid():
            student_group = form.save(commit=False)
            student_group.school = request.user.school
            student_group.save()
            return redirect('structure:student-group_list')
    else:
        form = StudentGroupForm(request=request)
    return render(request, 'structure/student-group-update.html', {'form': form})


def student_group_reject_student(request, pk, user_id):
    if request.method == 'POST':
        student_group = StudentGroup.objects.get(id=pk)
        student = CustomUser.objects.get(id=user_id)
        student_group.students.remove(student)
        return redirect(reverse('structure:student_group_detail', args=[pk]))
    else:
        return Http404()
    
    
    
def science_group_list(request):
    science_groups = ScienceGroup.objects.all()
    context = {
        'science_groups': science_groups
    }
    return render(request, 'structure/science-group.html', context)

def science_group_delete(request, pk):
    if request.method == 'POST':
        science_group = ScienceGroup.objects.get(id=pk)
        science_group.delete()
        return redirect('structure:science_group_list')
    else:
        return Http404()

def science_group_detail(request, id):
    science_group = ScienceGroup.objects.get(pk=id)
    context = {
        'science_group': science_group
    }
    return render(request, 'structure/science-group-detail.html', context)

def science_group_update(request, id):
    science_group = ScienceGroup.objects.get(pk=id)
    if request.method == 'POST':
        form = ScienceGroupForm(request.POST, instance=science_group, request=request)
        if form.is_valid():
            form.save()
            return redirect('structure:science_group_list')
    else:
        form = ScienceGroupForm(instance=science_group, request=request)
    return render(request, 'structure/science-group-update.html', {'form': form})

def science_group_create(request):
    if request.method == 'POST':
        form = ScienceGroupForm(request.POST, request=request)
        if form.is_valid():
            science_group = form.save(commit=False)
            science_group.school = request.user.school
            science_group.save()
            return redirect('structure:science-group_list')
    else:
        form = ScienceGroupForm(request=request)
    return render(request, 'structure/science-group-update.html', {'form': form})