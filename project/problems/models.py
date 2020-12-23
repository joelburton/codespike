from django.core import validators
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from core.models import StaffOnlyNotesModel, WorkflowModel


class Problem(StaffOnlyNotesModel, WorkflowModel, TimeStampedModel, models.Model):
    """A code problem."""

    _workflow_required = {
        "published": [
            "description",
            "code",
            "solution",
            "difficulty",
            "dri",
        ]
    }

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

    code = models.TextField(
        blank=True,
    )

    solution = models.TextField(
        blank=True,
    )

    explanation = models.TextField(
        blank=True,
    )

    difficulty = models.PositiveSmallIntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(10)],
        null=True,
        blank=True,
        help_text="From 1 to 10, where bigger is harder.",
    )

    # FIXME: relate to staff table
    dri = models.CharField(
        max_length=25,
        blank=True
    )

    source = models.CharField(
        max_length=255,
        blank=True,
        help_text="Credit for source of problem.",
    )

    def __str__(self):
        return self.title


class TestCase(StaffOnlyNotesModel, WorkflowModel, TimeStampedModel, models.Model):
    """Single test case for a problem."""

    class TestTypes(models.TextChoices):
        OUTPUT_EQ = 'output-eq', 'Output equals'
        OUTPUT_REGEX = 'output-regex', 'Output matches regex'
        RETURN_MATCH_JSON = 'return-match-json', 'Returns (tested with JSON)'
        JASMINE = 'jasmine', 'Jasmine test'

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=50,
    )

    type = models.CharField(
        max_length=25,
        choices=TestTypes.choices,
    )

    test = models.TextField()

    shown = models.BooleanField(
        default=True,
        verbose_name="Show to students?",
        help_text="Is this test shown to students?",
    )

    class Meta:
        unique_together = ['id', 'title']

    def __str__(self):
        return self.title


class StudentProblem(StaffOnlyNotesModel, TimeStampedModel, models.Model):
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
    )

    problem = models.ForeignKey(
        "problems.Problem",
        on_delete=models.CASCADE,
    )

    correct = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = ['student', 'problem']

    def get_absolute_url(self):
        return reverse("problem-detail", kwargs={"pk": self.id})


class StudentProblemSubmission(TimeStampedModel, models.Model):
    studentproblem = models.ForeignKey(
        "problems.StudentProblem",
        on_delete=models.CASCADE,
    )

    code = models.TextField()

    comment = models.TextField(
        help_text="Comments from student about submission.",
    )

    results = models.JSONField(
        help_text="JSON of results of test cases.",
        blank=True,
    )
