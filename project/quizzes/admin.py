from core.admin import WORKFLOW_ADMIN_ACTIONS
from django.contrib import admin
from django.utils.safestring import mark_safe
from quizzes.models import QuizProblem, Quiz, QuizStudent
from students.models import Student


class QuizProblemInline(admin.TabularInline):
    model = QuizProblem


class QuizStudentInline(admin.TabularInline):
    model = QuizStudent


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "st", "note"]
    inlines = [QuizProblemInline, QuizStudentInline]
    actions = WORKFLOW_ADMIN_ACTIONS

    def st(self, obj):
        if obj.status == "published":
            return '✅'
        if obj.status == "retired":
            return '⚠️'
        if obj.status == "private":
            return '❌'

    def note(self, obj):
        if obj.notes:
            return mark_safe(f"""<i title="{obj.notes}">🤔</i>""")


