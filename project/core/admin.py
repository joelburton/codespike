from django.contrib import messages
from django.contrib.admin import AdminSite
from django.contrib.messages import add_message
from django.core.exceptions import ValidationError
from django.db import transaction
from toolz import partial

from .models import WorkflowModel

AdminSite.site_header = '🦔 CodeSpike'


def set_status(status, modeladmin, request, queryset):
    """Action for administrative interface to publish.

    Note that this is intentionally implemented in a less efficient way; this could be
    done with a QuerySet method of::

      queryset.update(status='published')

    However, this does not emit post_save events, which are needed by our search indexing
    system---so we do it in a less-efficient way that does trigger this required update.
    """

    with transaction.atomic():
        for o in queryset.all():
            o.status = status
            try:
                o.full_clean()
                o.save()
            except ValidationError as e:
                # We can't publish this, so we'll let the user know via messages
                add_message(
                    request,
                    messages.ERROR,
                    "Could not publish %s (%s): %s" % (
                        str(o), o.pk, ", ".join(e.messages)))


WORKFLOW_ADMIN_ACTIONS = []
for state in WorkflowModel.WorkflowStates.values:
    fn = partial(set_status, state)
    fn.__name__ = state
    fn.short_description = f"Set workflow state to {state}"
    WORKFLOW_ADMIN_ACTIONS.append(fn)

