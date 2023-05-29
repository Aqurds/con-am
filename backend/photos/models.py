from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class PhotoPage(Page):
    """Page for a specific Photo"""

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image"),
        verbose_name=_("Image"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the photo"),
    )
    region = models.ForeignKey(
        "cms.Region",
        verbose_name=_("Region"),
        on_delete=models.SET_NULL,
        related_name="photos",
        null=True,
        blank=True,
        help_text=_("Region of the photo"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("image"),
        FieldPanel("image_alt_text"),
        FieldPanel("region"),
    ]


class PhotoIndexPage(Page):
    """Index page for photos"""

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )
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
    modal_download_image_button = models.CharField(
        _("Download Image Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for download image button"),
    )
    modal_usage_header = models.CharField(
        _("Usage Rights & Citation Header Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Usage Rights & Citation Header"),
    )
    modal_usage_description = RichTextField(
        _("Usage Description Text"),
        null=True,
        blank=True,
        help_text=_("Set text for Usage Description"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("introduction", classname="full"),
        MultiFieldPanel(
            [
                FieldPanel("modal_download_image_button"),
                FieldPanel("modal_usage_header"),
                FieldPanel("modal_usage_description"),
            ],
            heading="Translatable Photos Page Buttons and Text fields",
        ),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["PhotoPage"]

    def children(self):
        return self.get_children().specific().live()
