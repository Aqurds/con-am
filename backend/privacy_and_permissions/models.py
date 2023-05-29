from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class PrivacyPermissionsPage(Page):

    content_panels = Page.content_panels + [
        InlinePanel("privacy_permission_page_content", label="Content"),
    ]


class PrivacyPermissionContent(Orderable):
    page = ParentalKey(
        PrivacyPermissionsPage,
        on_delete=models.CASCADE,
        related_name="privacy_permission_page_content",
    )
    title = models.TextField(
        _("Title"),
        null=True,
        blank=True,
        help_text=_(
            "Title of the content. Example: 1. ACKNOWLEDGEMENT AND ACCEPTANCE OF TERMS"
        ),
    )
    content = RichTextField(
        _("Body"),
        null=True,
        blank=True,
        help_text=_("Content for the Privacy and Permissions Page"),
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("content"),
    ]
