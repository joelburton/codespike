from django.core.exceptions import ValidationError
from django.db import models
from model_utils.fields import StatusField, MonitorField
from model_utils.managers import QueryManager


class StaffOnlyNotesModel(models.Model):
    """Mixin for models with a staff-only note field."""

    notes = models.TextField(
        blank=True,
        verbose_name="Staff notes",
        help_text="These are never shown to students.",
    )

    class Meta:
        abstract = True


class TimeBoundModel(models.Model):
    """Mixin for models with a start and end date."""

    start_at = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )

    end_at = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    def clean(self):
        super().clean()
        if self.end_at and self.start_at:
            if self.end_at <= self.start_at:
                raise ValidationError({
                    "start_at": "End date must be after start date.",
                    "end_at": "End date must be after start date.",
                })


class WorkflowModel(models.Model):
    """Mixin for models that have a workflow state."""

    _workflow_required = {}

    class WorkflowStates(models.TextChoices):
        PRIVATE = 'private', 'Private'
        PUBLISHED = 'published', 'Published'
        RETIRED = 'retired', 'Retired'

    STATUS = WorkflowStates.choices

    status = StatusField(
        db_index=True,
        help_text='Hidden from students when private (visible, but not listed, when retired).',
    )

    status_changed = MonitorField(
        monitor='status',
        editable=False,
    )

    class Meta:
        abstract = True

    objects = QueryManager()
    private = QueryManager(status='private')
    published = QueryManager(status='published')
    retired = QueryManager(status='retired')
    public = QueryManager(status__in=['published', 'retired'])

    def clean(self):
        """Require that all state requirements are met."""

        super().clean()
        # noinspection PyUnresolvedReferences
        required = self._workflow_required.get(self.status)
        if not required:
            return True

        missing = {name: "Required to publish." for name in required if not getattr(self, name)}
        if missing:
            raise ValidationError(missing)
