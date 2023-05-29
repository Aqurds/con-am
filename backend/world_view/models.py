from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from django.utils.translation import ugettext_lazy as _


class WorldViewPage(Page):
    """Page for a specific world view"""

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
    world_view_url = models.CharField(
        _("World View URL"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the URL for World Views"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("World view image"),
        verbose_name=_("Image"),
    )

    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        ImageChooserPanel("image"),
        FieldPanel("world_view_url"),
    ]


class WorldViewIndexPage(Page):
    """Index page for World Views"""

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

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )
    search_input_placeholder = models.CharField(
        _("Search Input Placeholder Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Placeholder text for search input."),
    )
    search_button_text = models.CharField(
        _("Search Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the search button."),
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("search_input_placeholder"),
        FieldPanel("search_button_text"),

    ]

    # Can only have InitiativesPage children
    subpage_types = ["WorldViewPage"]

    def children(self):
        child = self.get_children().specific().live()
        return child.order_by("title")
