from core.admin import WORKFLOW_ADMIN_ACTIONS
from django.contrib import admin
from django.utils.safestring import mark_safe
from problems.models import TestCase, Problem, StudentProblem, StudentProblemSubmission


class ProblemTestCaseInline(admin.StackedInline):
    model = TestCase
    extra = 0


class ProblemStudentInline(admin.StackedInline):
    model = StudentProblem
    extra = 0


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "difficulty", 'st', 'note']
    inlines = [ProblemTestCaseInline, ProblemStudentInline]
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

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'problem', 'title', 'st', 'note']

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


class ProblemStudentSubmissionInline(admin.TabularInline):
    model = StudentProblemSubmission
    extra = 0


@admin.register(StudentProblem)
class ProblemStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'problem', 'student', 'note']
    inlines = [ProblemStudentSubmissionInline]

    def note(self, obj):
        if obj.notes:
            return mark_safe(f"""<i title="{obj.notes}">🤔</i>""")


@admin.register(StudentProblemSubmission)
class ProblemStudentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'studentproblem', 'created']