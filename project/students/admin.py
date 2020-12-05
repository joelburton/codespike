from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from quizzes.models import Quiz, QuizStudent

from .models import Student


class QuizStudentInline(admin.TabularInline):
    model = QuizStudent

@admin.register(Student)
class StudentAdmin(UserAdmin):
    """Student admin.

    This subclasses user admin, so adding a student is a single step. This only adds fields
    specific to students.
    """

    inlines = [QuizStudentInline]
