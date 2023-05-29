from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class InitiativesPage(Page):
    """Initiatives Page"""

    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Header image that is going to be displayed for the page"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image of the page"),
    )
    initiative_name = models.CharField(
        _("Initiative Name"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Name of Initiative"),
    )
    short_description = models.TextField(
        _("Short Description"),
        null=True,
        blank=True,
        help_text=_("Short description of Initiative"),
    )
    initiative_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Initiative image"),
    )
    initiative_image_alt_text = models.CharField(
        _("Initiative Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the initiative image"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        StreamFieldPanel("initiative_name"),
        StreamFieldPanel("short_description"),
        ImageChooserPanel("initiative_image"),
    ]

    additional_search_fields = [
        index.SearchField("initiative_name", partial_match=True),
        index.SearchField("short_description", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class InitiativeIndexPage(Page):

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
    ]

    additional_search_fields = [
        index.SearchField("introduction", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    # Can only have InitiativesPage children
    subpage_types = ["InitiativesPage"]

    def children(self):
        return self.get_children().specific().live()
