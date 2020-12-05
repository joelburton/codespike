from core.models import StaffOnlyNotesModel, WorkflowModel
from django.db import models
from model_utils.models import TimeStampedModel, TimeFramedModel


class Quiz(StaffOnlyNotesModel, WorkflowModel, TimeStampedModel, models.Model):
    id = models.SlugField(
        max_length=25,
        primary_key=True,
    )

    title = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    # FIXME: to staff
    dri = models.CharField(
        max_length=25,
    )

    problems = models.ManyToManyField(
        "problems.Problem",
        through="quizzes.QuizProblem",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quizzes"


class QuizProblem(StaffOnlyNotesModel, WorkflowModel, TimeStampedModel, models.Model):
    quiz = models.ForeignKey(
        "quizzes.Quiz",
        # make sense to be able to delete a quiz and have the associations for it disappear
        on_delete=models.CASCADE,
    )

    problem = models.ForeignKey(
        "problems.Problem",
        # does not make sense to delete related problems when a problem goes away --- this should
        # be done by hand
        on_delete=models.RESTRICT,
    )

    order = models.PositiveSmallIntegerField(
        default=1,
    )

    class Meta:
        unique_together = ['quiz', 'problem']


class QuizStudent(StaffOnlyNotesModel, WorkflowModel, TimeStampedModel, TimeFramedModel, models.Model):
    quiz = models.ForeignKey(
        "quizzes.Quiz",
        on_delete=models.CASCADE,
    )

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
    )

    def percent_correct(self):
        raise NotImplementedError

