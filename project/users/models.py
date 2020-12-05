from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser):
    """Site user: a single person, be they student, staff, or other.

    Everyone will have a record here --- this is primarily intended for students and staff, but if
    we had someone (say, a vendor) who needed an account, they'd have a record here.

    As this system grows, we may have people who are significant to Rithm but not users of the site
    (like an applicant, who is not yet a user). They'd still get a record here, and they would be
    marked as not active, so they couldn't try to log in.
    """

    # username
    # password
    # is_staff
    # is_active
    # date_joined

    is_student = models.BooleanField(
        default=True,
    )

    username = models.CharField(
        'username',
        max_length=50,
        primary_key=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[UnicodeUsernameValidator()],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    # =================================================================== names

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    # ================================================================= contact

    email = models.EmailField(
        verbose_name='Email address',
    )

    @property
    def title(self):
        return self.get_full_name()

    @property
    def full_name(self):
        return self.get_full_name()

    # @property
    # def get_absolute_url(self):
    #     return reverse('user_profile', kwargs={'pk': self.username })
