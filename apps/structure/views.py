from django.shortcuts import render, redirect
from django.http import Http404

from .models import AcademicYear, Kafedra, LessonTime, Science
from .forms import AcademicYearForm, KafedraForm, LessonTimeForm, ScienceForm


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