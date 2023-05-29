from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from modelcluster.fields import ParentalKey

from django.db import models
from django.utils.translation import ugettext_lazy as _


class VideoPage(Page):
    """Page for a specific video"""

    embed_url = models.CharField(
        _("Embed URL"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(
            "This needs to be the embed URL of the video or else the video player will not work"
        ),
    )
    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Thumbnail image that is going to be displayed for the video"),
    )
    thumbnail_image_alt_text = models.CharField(
        _("Thumbnail Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the thumbnail image"),
    )
    description = models.TextField(
        _("Description"), null=True, blank=True, help_text=_("Description of the video")
    )

    content_panels = Page.content_panels + [
        FieldPanel("embed_url"),
        ImageChooserPanel("thumbnail_image"),
        FieldPanel("description"),
    ]

    additional_search_fields = [
        index.SearchField("description", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class VideoIndexPage(Page):
    """Index page for videos"""

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
    media_hub_section_header_title = models.CharField(
        _("Media Hub Section Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Media Hub Section Header Title"),
    )
    register_button = models.CharField(
        _("Register Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for Register Button Text"),
    )
    login_button = models.CharField(
        _("Login Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for Login Button Text"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        MultiFieldPanel(
            [
                FieldPanel("media_hub_section_header_title"),
                FieldPanel("register_button"),
                FieldPanel("login_button"),
                InlinePanel(
                    "media_hub_videos_list",
                    label=_("Media Hub List"),
                ),
            ],
            heading="Translatable Videos Page Buttons and Text fields",
        ),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["VideoPage"]

    def children(self):
        return self.get_children().specific().live()


class VideosMediaHub(Orderable):
    page = ParentalKey(
        VideoIndexPage,
        on_delete=models.CASCADE,
        related_name="media_hub_videos_list",
    )
    media_hub_item = models.CharField(
        _("Media Hub Item"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Media Hub Item"),
    )
