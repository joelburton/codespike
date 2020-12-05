from core.models import WorkflowModel
from django.contrib.auth.models import UserManager
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

from users.models import User


class StaffManager(UserManager):
    """Can get only "staff" from StaffMember model."""
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_staff=True)


class StaffMember(User):
    """Staff member."""

    objects = StaffManager()

    class Meta:
        proxy = True
        verbose_name = "staff member"

    def get_absolute_url(self):
        return reverse('staff_detail', kwargs={'slug': self.username})
