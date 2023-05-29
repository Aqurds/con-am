from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class GoPage(Page):
    """Page for Go"""

    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Header image"),
        verbose_name=_("Header Image"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    header_title = models.CharField(
        _("Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text that will be shown in the header of the page"),
    )
    header_content = models.TextField(
        _("Header Content"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown below the header title"),
    )

    # Take the quiz section
    are_you_called_button = models.CharField(
        _("Are you Called Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_(
            "Are you called button text that will be shown in the take the quiz section"
        ),
    )
    take_the_quiz_button = models.CharField(
        _("Take The Quiz Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Take the quiz button text that will be shown"),
    )
    has_quiz = models.BooleanField(
        _("Has Quiz"),
        default=False,
        null=True,
        help_text=_("Set this as true to display the Take the Quiz section in Go Page"),
    )

    # Ways You Can Serve Section
    ways_to_serve_title = models.CharField(
        _("Ways To Serve Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text that will be shown in the Ways to Serve section"),
    )
    ways_to_serve_bottom_text = models.TextField(
        _("Ways To Serve Bottom Text"),
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown at the bottom part of the title in the Ways To Serve section"
        ),
    )
    short_term_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the first section short term"),
        verbose_name=_("Short Term Image"),
    )
    short_term_image_alt_text = models.CharField(
        _("Short Term Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the short term image"),
    )
    one_to_two_year_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the one to two year"),
        verbose_name=_("One to Two Year Image"),
    )
    one_to_two_year_image_alt_text = models.CharField(
        _("One To Two Year Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the one to two year image"),
    )
    career_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the career"),
        verbose_name=_("Career Image"),
    )
    career_image_alt_text = models.CharField(
        _("Career Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the career image"),
    )
    short_term_text = models.CharField(
        _("Short Term Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for Short Term"),
    )
    one_to_two_year_text = models.CharField(
        _("One to Two Year Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for One to Two Year"),
    )
    career_text = models.CharField(
        _("Career Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for Career"),
    )

    # TODO Ask for context about the START JOURNEY button

    stories_section = models.ForeignKey(
        "stories.StoryIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Stories section of the page"),
        verbose_name=_("Stories Section"),
    )
    stories_header_title = models.CharField(
        _("Stories Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Stories Header"),
    )
    stories_header_sub_title = models.CharField(
        _("Stories Header Sub Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Stories Header Sub Title"),
    )
    stories_read_all_button_text = models.CharField(
        _("Stories Read All Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Stories Read All Button"),
    )

    # Start your Journey
    start_your_journey_title = models.CharField(
        _("Start Your Journey Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown as the title of the Start Your Journey section"
        ),
    )
    start_your_journey_content = models.CharField(
        _("Start Your Journey Content"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown as the content under the title of the Start Your Journey section"
        ),
    )
    start_your_journey_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown start your journey background"),
        verbose_name=_("Start Your Journey Background Image"),
    )
    start_your_journey_background_image_alt_text = models.CharField(
        _("Start Your Journey Background Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the start your journey background image"),
    )
    start_your_journey_first_button_name = models.CharField(
        _("Start Your Journey First Button Name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Set the name of the first button"),
    )
    start_your_journey_second_button_name = models.CharField(
        _("Start Your Journey Second Button Name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Set the name of the second button"),
    )
    start_your_journey_third_button_name = models.CharField(
        _("Start Your Journey Third Button Name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Set the name of the third button"),
    )

    header_section_video_url = models.TextField(
        _("Video URL"),
        null=True,
        blank=True,
        help_text=_(
            "URL of the video to be shown in the header section. This needs to be the EMBED url of the video or else it will not work properly"
        ),
    )
    header_section_thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("This serves as the thumbnail of the header section video"),
    )
    header_section_thumbnail_alt_text = models.CharField(
        _("Thumbnail Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the thumbnail"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                FieldPanel("header_title"),
                FieldPanel("header_content"),
                FieldPanel("header_section_video_url"),
                ImageChooserPanel("header_section_thumbnail"),
                FieldPanel("header_section_thumbnail_alt_text"),
            ],
            heading=_("Header Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("are_you_called_button"),
                FieldPanel("take_the_quiz_button"),
                FieldPanel("has_quiz"),
            ],
            heading=_("Take the Quiz section"),
        ),
        MultiFieldPanel(
            [
                InlinePanel("go_gallery", label="Gallery"),
            ],
            heading=_("Gallery section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("ways_to_serve_title"),
                FieldPanel("ways_to_serve_bottom_text"),
                ImageChooserPanel("short_term_image"),
                FieldPanel("short_term_image_alt_text"),
                ImageChooserPanel("one_to_two_year_image"),
                FieldPanel("one_to_two_year_image_alt_text"),
                ImageChooserPanel("career_image"),
                FieldPanel("career_image_alt_text"),
                FieldPanel("short_term_text"),
                FieldPanel("one_to_two_year_text"),
                FieldPanel("career_text"),
            ],
            heading=_("Ways You Can Serve Section"),
        ),
        MultiFieldPanel(
            [
                PageChooserPanel("stories_section"),
                FieldPanel("stories_header_title"),
                FieldPanel("stories_header_sub_title"),
                FieldPanel("stories_read_all_button_text"),
            ],
            heading=_("Stories Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("start_your_journey_title"),
                FieldPanel("start_your_journey_content"),
                ImageChooserPanel("start_your_journey_background_image"),
                FieldPanel("start_your_journey_background_image_alt_text"),
                FieldPanel("start_your_journey_first_button_name"),
                FieldPanel("start_your_journey_second_button_name"),
                FieldPanel("start_your_journey_third_button_name"),
            ],
            heading=_("Start Your Journey Section"),
        ),
    ]
    additional_search_fields = [
        index.SearchField("header_title", partial_match=True),
        index.SearchField("header_content", partial_match=True),
        index.SearchField("ways_to_serve_title", partial_match=True),
        index.SearchField("ways_to_serve_bottom_text", partial_match=True),
        index.SearchField("start_your_journey_title", partial_match=True),
        index.SearchField("start_your_journey_content", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    class Meta:
        verbose_name = _("Go Page")
        verbose_name_plural = _("Go Pages")


class SpecialGivingPageGallery(Orderable):
    page = ParentalKey(
        GoPage,
        on_delete=models.CASCADE,
        related_name="go_gallery",
    )
    is_video = models.BooleanField(
        _("Is Video"),
        default=False,
        help_text=_("Set this as true if the item in the gallery is a Video"),
    )
    video_url = models.TextField(
        _("Video URL"),
        null=True,
        blank=True,
        help_text=_(
            "URL of the video to be shown. This needs to be the EMBED url of the video or else it will not work properly"
        ),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image for the go page gallery. This also serves as the thumbnail if the item of the gallery is a video"
        ),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )

    panels = [
        FieldPanel("is_video"),
        FieldPanel("video_url"),
        ImageChooserPanel("image"),
        FieldPanel("image_alt_text"),
    ]
