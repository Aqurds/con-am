from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey

from django.db import models
from django.utils.translation import ugettext_lazy as _


class StoryPage(Page):
    """Page for a specific story"""

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Image"),
        help_text=_("Image for the story"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )
    region = models.ForeignKey(
        "cms.Region",
        verbose_name=_("Region"),
        on_delete=models.SET_NULL,
        related_name="stories",
        null=True,
        blank=True,
        help_text=_("Region of the story"),
    )
    body = RichTextField(
        _("Body"),
        null=True,
        blank=True,
        help_text=_("Body of the story"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("image"),
        FieldPanel("image_alt_text"),
        FieldPanel("region"),
        FieldPanel("body"),
    ]

    additional_search_fields = [
        index.SearchField("region__title", partial_match=True),
        index.SearchField("body", partial_match=True),
        index.SearchField("simple_prayer", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    parent_page_types = ["stories.StoryIndexPage"]


class StoryIndexPage(Page):
    """Index page for stories"""

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
    story_page_explore_button_text = models.CharField(
        _("Story Page Explore Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Explore button text at the end of every displayed story page."),
    )
    simple_prayer_header = models.CharField(
        _("Simple Prayer Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text in the todays simple prayer section"),
    )
    simple_prayer = RichTextField(
        _("Simple Prayer"),
        null=True,
        blank=True,
        help_text=_("Prayer that will be displayed under the 'Todays simple prayer'"),
    )
    giving_initiative_header = models.CharField(
        _("Giving Initiative Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text shown in giving initiative section."),
    )
    giving_initiative_content = models.TextField(
        _("Giving Initiative Content"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Giving initiative content shown under the header."),
    )
    giving_initiative_button_text = models.CharField(
        _("Giving Initiative Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Button text in the giving initiave section."),
    )
    story_slider_read_more_text = models.CharField(
        _("Story Pages Read More Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Read more text for each story in story slider."),
    )
    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("story_page_explore_button_text"),
        InlinePanel("story_slider_headers", heading="Stories Slider Header Text"),
        FieldPanel("story_slider_read_more_text"),
        MultiFieldPanel(
            [
                FieldPanel("simple_prayer_header"),
                FieldPanel("simple_prayer"),
            ], 
            heading="Simple Prayer Section Details for Story Pages"
        ),
        MultiFieldPanel(
            [
                FieldPanel("giving_initiative_header"),
                FieldPanel("giving_initiative_content"),
                FieldPanel("giving_initiative_button_text"),
            ], 
            heading="Giving Initiative Details for Story Pages"
        ),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["StoryPage"]

    def children(self):
        return self.get_children().specific().live()


class StorySliderHeader(Orderable):
    """Slider Header Text"""

    story_slider = ParentalKey(
        "StoryIndexPage",
        related_name="story_slider_headers",
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Story Slider Header"),
        help_text=_("Page assigned to header text."),
    )

    slider_header_text = models.CharField(
        _("Story Slider Header Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text above stories slider."),
    )

    slider_header_text_es = models.CharField(
        _("Story Slider Header Text in Spanish"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text above stories slider in Spanish page."),
    )

    slider_subheader_text = models.CharField(
        _("Story Slider Subheader Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Subheader text above stories slider."),
    )

    slider_subheader_text_es = models.CharField(
        _("Story Slider Subheader Text in Spanish"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Subheader text above stories slider in Spanish."),
    )

    slider_header_read_all_button = models.CharField(
        _("Story Slider Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Button text above stories slider."),
    )

    slider_header_read_all_button_es = models.CharField(
        _("Story Slider Button Text in Spanish"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Button text above stories slider in Spanish."),
    )
