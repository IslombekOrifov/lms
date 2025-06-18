from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from lms.apps.account.models import CustomUser


LANGUAGES = (
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English')
)

ROOM_GROUP_TYPE = (
    ('none', 'None'),
    ('labs', 'Labs'),
    ('practical', 'Practical'),
    ('lecture', 'Lecture'),
)

class AcademicYear(MPTTModel, models.Model):
    name = models.CharField(max_length=223)
    season = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(null=True, blank=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='childs'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name}"

    
class Kafedra(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    department_user = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='departments')
    school = models.ForeignKey('main.School', on_delete=models.CASCADE, related_name='kafedras')

    def __str__(self):
        return f"{self.name}"
    

class LessonTime(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    school = models.ForeignKey('main.School', on_delete=models.CASCADE, related_name='lesson_times')

    def __str__(self):
        return f"{self.name}"


class Science(MPTTModel, models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    academic_year = models.ForeignKey('structure.AcademicYear', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True)
    kafedra = models.ForeignKey('structure.Kafedra', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='direction_science')
    which_semester = models.IntegerField(null=True, blank=True)

    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='childs'
    )
    school = models.ForeignKey('main.School', on_delete=models.CASCADE, related_name='sciences')


    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name}"


class StudentGroup(models.Model):
    name = models.CharField(max_length=223)
    lang = models.CharField(max_length=2, choices=LANGUAGES)
    science_type = models.CharField(max_length=10, choices=ROOM_GROUP_TYPE, null=True, blank=True)
    school = models.ForeignKey('main.School', on_delete=models.CASCADE, related_name='student_groups')
    tyutor = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="groupmodel_to_tyutor")
    students = models.ManyToManyField(CustomUser)
    academic_year = models.ForeignKey('structure.AcademicYear', on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="groupmodel_to_academic_year")
    is_active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name


class ScienceGroup(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    science = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='science_to_group')
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='groupmodel_to_science')
    teacher = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='scheduletable_to_teacher')
    is_active = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"


class ScheduleTable(models.Model):
    week_day = models.CharField(max_length=223, null=True, blank=True)
    lesson_time = models.ForeignKey(LessonTime, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='scheduletable_to_lessontime')
    department = models.ForeignKey('structure.Kafedra', on_delete=models.SET_NULL, null=True, blank=True,
                                   limit_choices_to={'level': 1},
                                   related_name='scheduletable_to_department')
    teacher = models.ForeignKey('account.CustomUser', on_delete=models.SET_NULL, null=True,
                                related_name='scheduletable_to_employee')
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True,
                              related_name='scheduletable_to_groupmodel')
    semester = models.ForeignKey('structure.AcademicYear', on_delete=models.SET_NULL, null=True,
                                 related_name='scheduletable_to_semester')

    def __str__(self):
        return f"{self.teacher} - {self.para}"



