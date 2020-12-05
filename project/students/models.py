from django.contrib.auth.models import UserManager

from users.models import User


# resume_path = None


class StudentManager(UserManager):
    """Restrict Student model to just users who are students."""

    def get_queryset(self):
        return super().get_queryset().filter(is_student=True)


class Student(User):
    """Student."""

    objects = StudentManager()

    class Meta:
        proxy = True
        verbose_name = "student"
