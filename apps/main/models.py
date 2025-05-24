from django.db import models
from account.models import CustomUser
from structure.models import ROOM_GROUP_TYPE, LANGUAGES, StudentGroup, ScienceGroup

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

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
    title = models.CharField(max_length=225)
    source = models.FileField(upload_to='task_source/')
    deadline = models.DateTimeField(null=True, blank=True)
    grade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Submission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, related_name='submission_to_task')
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='submissions_to_student')
    source = models.FileField(upload_to='submissions/', null=True, blank=True)
    grade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Submission #{self.id}"


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    lesson_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=LESSON_STATUS_CHOICES, null=True, blank=True, max_length=223)
    groups = models.ForeignKey(ScienceGroup, on_delete=models.SET_NULL, null=True,related_name='lesson_to_group_model')

    def __str__(self):
        return self.name



class LessonSource(models.Model):
    teacher = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='lessonsource_to_teacher')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='lessonsource_to_lesson')
    file = models.FileField(upload_to='lesson_sources/')

    def __str__(self):
        return f"LessonSource #{self.id}"


class NB(models.Model):
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True, related_name='nb_to_student')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, related_name='nb_to_lesson')
    cause_status = models.BooleanField(null=True, blank=True)
    type_cause = models.CharField(max_length=255, null=True, blank=True)
    cause_file = models.FileField(upload_to='cause_file/', null=True, blank=True)

    def __str__(self):
        return f"NB #{self.id} - {self.student}"


class RatingNotebook(models.Model):
    student = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='ratingnotebook_to_student')
    science_name = models.ForeignKey('structure.Science', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name="individual_plans", limit_choices_to={'level': 1})
    credit = models.IntegerField(null=True, blank=True)
    semester = models.ForeignKey('structure.AcademicYear', on_delete=models.SET_NULL, null=True,
                                 related_name='ratingnotebook_to_semester')
    grade = models.DecimalField(max_digits=10, decimal_places=2)  # 2,..5
    ball = models.DecimalField(max_digits=10,
                               decimal_places=2)
    comment = models.CharField(max_length=255, null=True,
                               blank=True)

    def __str__(self):
        return f"RatingNotebook #{self.id}"