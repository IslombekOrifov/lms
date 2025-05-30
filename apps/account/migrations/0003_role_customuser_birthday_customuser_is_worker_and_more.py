# Generated by Django 5.2 on 2025-05-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_customuser_is_archived"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("admin", "Administrator"),
                            ("dekan", "Dean"),
                            ("rector", "Rector"),
                            ("department_user", "Department User"),
                            ("tutor", "Tutor"),
                            ("stylist", "Stylist"),
                            ("accountant", "Accountant"),
                            ("teacher", "Teacher"),
                            ("student", "Student"),
                        ],
                        max_length=50,
                        unique=True,
                        verbose_name="Role Name",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
            options={
                "verbose_name": "Role",
                "verbose_name_plural": "Roles",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="customuser",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_worker",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="middle_name",
            field=models.CharField(blank=True, max_length=223, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="start_work",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.ManyToManyField(blank=True, to="account.role"),
        ),
    ]
