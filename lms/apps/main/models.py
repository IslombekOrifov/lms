from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

from lms.apps.account.models import CustomUser
from lms.apps.structure.models import ROOM_GROUP_TYPE, LANGUAGES, StudentGroup, ScienceGroup


class School(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='school/logo/', blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        
    def __str__(self):
        return f"{self.name}"


LESSON_STATUS_CHOICES = (
    ('otildi', 'Otildi'),
    ('otilmadi', 'Otilmadi'),
    ('qoldirildi', 'Qoldirildi'),
)


class Task(models.Model):
    group = models.ForeignKey(ScienceGroup, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='task_to_group')
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='task_to_lesson')
    title = models.CharField(max_length=225)
    source = models.FileField(upload_to='task_source/')
    deadline = models.DateTimeField(null=True, blank=True)
    grade = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title


class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, related_name='submission_to_task')
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='submissions_to_student')
    source = models.FileField(upload_to='submissions/', null=True, blank=True)
    grade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Submission #{self.id}"


class Module(models.Model):
    group = models.ForeignKey(ScienceGroup,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}. {self.title}'


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    lesson_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=LESSON_STATUS_CHOICES, null=True, blank=True, max_length=223)
    module = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True,related_name='lesson_to_group_model')
    about = models.CharField(max_length=255, blank=True, null=True)
    text = RichTextField(config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class DailyRatings(models.Model):
    science_group = models.ForeignKey(ScienceGroup,
                               related_name='daily_taings',
                               on_delete=models.CASCADE)
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='dailyrating_to_student')
    ball = models.DecimalField(max_digits=10,
                               decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.science_group} > {self.student}'


class NBandRating(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='nb_and_rating_to_lesson')
    is_checked = models.BooleanField(default=False)
    is_rated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LessonSource(models.Model):
    teacher = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='lessonsource_to_teacher')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='lessonsource_to_lesson')
    file = models.FileField(upload_to='lesson_sources/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"LessonSource #{self.id}"


class NB(models.Model):
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True, related_name='nb_to_student')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, related_name='nb_to_lesson')
    cause_status = models.BooleanField(null=True, blank=True)
    type_cause = models.CharField(max_length=255, null=True, blank=True)
    cause_file = models.FileField(upload_to='cause_file/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"NB #{self.id} - {self.student}"


class RatingNotebook(models.Model):
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='ratingnotebook_to_student')
    science_name = models.ForeignKey('structure.Science', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name="individual_plans", limit_choices_to={'level': 1})
    semester = models.ForeignKey('structure.AcademicYear', on_delete=models.SET_NULL, null=True,
                                 related_name='ratingnotebook_to_semester')
    grade = models.DecimalField(max_digits=10, decimal_places=2)  # 2,..5
    ball = models.DecimalField(max_digits=10,
                               decimal_places=2)
    comment = models.CharField(max_length=255, null=True,
                               blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"RatingNotebook #{self.id}"