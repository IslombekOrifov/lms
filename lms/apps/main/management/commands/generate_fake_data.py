# your_app/management/commands/generate_fake_data.py

import random
import uuid
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker

from account.models import CustomUser, Role
from main.models import School
from structure.models import AcademicYear, Kafedra, Science, StudentGroup, ScienceGroup


fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for testing'

    def handle(self, *args, **kwargs):
        # Создаем школу
        school, _ = School.objects.get_or_create(
            name="Test School",
            defaults={
                "address": fake.address(),
                "phone": fake.phone_number(),
                "email": fake.email()
            }
        )

        # Создаем роли
        Role.create_default_roles()
        roles = Role.objects.all()

        # Создаем преподавателей
        teachers = []
        for _ in range(10):
            role = roles.filter(name='teacher').first()
            teacher = CustomUser.objects.create_user(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                middle_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                birthday=fake.date_of_birth(minimum_age=25, maximum_age=60),
                role=role,
                custom_uuid=uuid.uuid4(),
                school=school,
                is_worker=True
            )
            teachers.append(teacher)

        # Создаем студентов
        students = []
        student_role = roles.filter(name='student').first()
        for _ in range(50):
            student = CustomUser.objects.create_user(
                username=fake.user_name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                middle_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                birthday=fake.date_of_birth(minimum_age=18, maximum_age=25),
                role=student_role,
                custom_uuid=uuid.uuid4(),
                school=school,
                is_worker=False
            )
            students.append(student)

        # Создаем учебный год
        semester, _ = AcademicYear.objects.get_or_create(
            name="2024-2025",
            defaults={
                "start_date": datetime.today(),
                "end_date": datetime.today() + timedelta(days=365),
                "is_active": True
            }
        )

        # Создаем кафедру
        kafedra, _ = Kafedra.objects.get_or_create(
            name="Informatika",
            school=school,
            department_user=random.choice(teachers)
        )

        # Создаем науки
        sciences = []
        for _ in range(5):
            science = Science.objects.create(
                name=fake.job(),
                academic_year=semester,
                kafedra=kafedra,
                is_active=True,
                which_semester=random.randint(1, 8)
            )
            sciences.append(science)

        # Создаем учебные группы
        student_groups = []
        for i in range(3):
            group = StudentGroup.objects.create(
                name=f"Group-{i+1}",
                lang="uz",
                science_type="lecture",
                school=school,
                tyutor=random.choice(teachers),
                semester=semester
            )
            group.students.set(random.sample(students, 15))
            student_groups.append(group)

        # Создаем научные группы
        for group in student_groups:
            for science in sciences:
                ScienceGroup.objects.create(
                    name=f"{group.name}-{science.name}",
                    code=f"S{random.randint(100, 999)}",
                    science=science,
                    group=group,
                    teacher=random.choice(teachers)
                )

        self.stdout.write(self.style.SUCCESS("✅ Fake data generated successfully!"))
