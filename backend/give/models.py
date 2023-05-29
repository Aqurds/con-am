from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    InlinePanel,
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SpecialGivingPage(Page):
    TYPE_REGIONAL = "regional"
    TYPE_GENERAL = "general"
    TYPE_EXECUTIVE = "executive"
    TYPE_SPECIAL = "special"

    TYPE_CHOICES = [
        (TYPE_REGIONAL, "Regional"),
        (TYPE_GENERAL, "General"),
        (TYPE_EXECUTIVE, "Executive"),
        (TYPE_SPECIAL, "Special"),
    ]

    #
    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown as the thumbnail in the slider of the give page"
        ),
    )
    thumbnail_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the thumbnail image"),
    )
    # Header Section
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown in the header portion of the page"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    header_title_text = models.CharField(
        _("Header Title Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text of the title that will be shown on the header. Example ('Disaster Relief')"
        ),
    )
    header_title_description = models.TextField(
        _("Header Title Description"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown below the header title text"),
    )
    # First Section
    first_section_title = models.CharField(
        _("First Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title of the first content section of the page. Example 'AGWM Responds to double disasters on two continents'"
        ),
    )
    first_section_content = models.TextField(
        _("First Section Content"),
        null=True,
        blank=True,
        help_text=_("Content under the first section title."),
    )

    # Give Section
    give_section_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image shown as the background image for the give section of the page"
        ),
    )
    give_section_background_image_alt_text = models.CharField(
        _("Give Section Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the give section background image"),
    )
    give_section_icon_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image shown as the icon image for the give section of the page"),
    )
    give_section_icon_image_alt_text = models.CharField(
        _("Give Section Icon Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the give section icon image"),
    )
    give_section_title = models.CharField(
        _("Give Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title that will be shown in the give section of the page"),
    )
    give_section_content = models.TextField(
        _("Give Section Content"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown as content under the give section title"),
    )
    # Second Section
    second_section_title = models.CharField(
        _("Second Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title that will be shown in the second content section of the page. Example 'AGWM Responds to double disasters on two continents'"
        ),
    )
    second_section_content = RichTextField(
        _("Second Section Content"),
        null=True,
        blank=True,
        help_text=_("Content that will be shown under the second section title"),
    )
    # Other fields
    giving_link_url = models.TextField(
        _("Giving Link URL"),
        null=True,
        blank=True,
        help_text=_("Giving Link URL for the specific dedicated giving page"),
    )
    page_type = models.CharField(
        _("Page Type"),
        choices=TYPE_CHOICES,
        max_length=100,
        null=True,
        help_text=_("Type of Giving Initiatives"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("page_type"),
        ImageChooserPanel("thumbnail_image"),
        FieldPanel("thumbnail_image_alt_text"),
        MultiFieldPanel(
            [
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                FieldPanel("header_title_text"),
                FieldPanel("header_title_description"),
            ],
            heading=_("Header Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("first_section_title"),
                FieldPanel("first_section_content"),
            ],
            heading=_("First Section"),
        ),
        InlinePanel("special_giving_page_images", label="Images"),
        MultiFieldPanel(
            [
                FieldPanel("second_section_title"),
                FieldPanel("second_section_content"),
            ],
            heading=_("Second Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("give_section_background_image"),
                FieldPanel("give_section_background_image_alt_text"),
                ImageChooserPanel("give_section_icon_image"),
                FieldPanel("give_section_icon_image_alt_text"),
                FieldPanel("give_section_title"),
                FieldPanel("give_section_content"),
            ],
            heading=_("Give Section"),
        ),
        FieldPanel("giving_link_url"),
    ]
    additional_search_fields = [
        index.SearchField("header_title_text", partial_match=True),
        index.SearchField("header_title_description", partial_match=True),
        index.SearchField("first_section_title", partial_match=True),
        index.SearchField("first_section_content", partial_match=True),
        index.SearchField("second_section_title", partial_match=True),
        index.SearchField("second_section_content", partial_match=True),
        index.SearchField("give_section_title", partial_match=True),
        index.SearchField("give_section_content", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    parent_page_types = ["give.SpecialGivingIndexPage"]

    class Meta:
        verbose_name = _("Giving Initiative")
        verbose_name_plural = _("Giving Initiatives")


class SpecialGivingPageGallery(Orderable):
    page = ParentalKey(
        SpecialGivingPage,
        on_delete=models.CASCADE,
        related_name="special_giving_page_images",
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
            "Image of the special giving page. This also serves as the thumbnail if the item of the gallery is a video"
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


class SpecialGivingIndexPage(Page):
    """Index Page for the Special Giving Page"""

    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown in the header portion of the page"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["SpecialGivingPage"]

    def children(self):
        return self.get_children().specific().live()


class GivePage(Page):
    # Header Section
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown in the header portion of the page"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    header_side_text = models.CharField(
        _("Header Side Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown on the left side of the header of the page"
        ),
    )
    header_title_text = models.CharField(
        _("Header Title Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text of the title that will be shown on the right side of the header. Example ('Live Dead Africa')"
        ),
    )
    header_title_description = models.TextField(
        _("Header Title Description"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown below the header title text"),
    )
    missionary_page = models.ForeignKey(
        "individual_missionaries.IndividualMissionaryIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Individual Missionary page"),
        verbose_name=_("Missionary Page"),
    )

    # First section
    first_section_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown in the first section or the 'Find a Missionary' portion of the page"
        ),
    )
    first_section_image_alt_text = models.CharField(
        _("First Section Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the first section image"),
    )
    first_section_title = models.CharField(
        _("First Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown in the first section of the page. Example 'Find a Missionary'"
        ),
    )
    # Initiatives Section
    special_give_index_page = models.ForeignKey(
        "give.SpecialGivingIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Special Giving Index Page"),
        verbose_name=_("Special Giving Index Page"),
    )
    initiatives_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background Image that will be shown in the initiatives section of the page"
        ),
    )
    initiatives_background_image_alt_text = models.CharField(
        _("Initiatives Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the initiatives background image"),
    )
    # initiatives_title = models.CharField(
    #     _("Initiatives Title"),
    #     max_length=255,
    #     null=True,
    #     blank=True,
    #     help_text=_(
    #         "Title text that will be shown in the initiatives section of the page"
    #     ),
    # )
    slider_header_text = models.CharField(
        _("Slider Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text for the giving initiative slider section"),
    )

    # Second Section
    second_section_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown in the second section or the 'Senders Fund' portion of the page"
        ),
    )
    second_section_image_alt_text = models.CharField(
        _("Section Section Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the second section image"),
    )
    second_section_dedicated_page = models.ForeignKey(
        "give.SpecialGivingPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Dedicated page or special giving page of the second section of the page"
        ),
        verbose_name=_("Second Section Dedicated Page"),
    )
    # Other fields
    is_legacy_page_external = models.BooleanField(
        _("Is Legacy Page External"),
        default=False,
        help_text=_(
            "Checkbox for determining whether the Legacy Giving button is an external page or not"
        ),
    )
    legacy_giving_external_url = models.CharField(
        _("Legacy Giving External URL"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("URL for cases where the Legacy Page is external"),
    )
    legacy_giving_page = models.ForeignKey(
        "legacy.LegacyPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Legacy Giving page"),
        verbose_name=_("Legacy Giving Page"),
    )
    legacy_giving_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown for the legacy giving section of the page"
        ),
    )
    legacy_giving_image_alt_text = models.CharField(
        _("Legacy Giving Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the legacy giving image"),
    )
    giving_faq_page = models.ForeignKey(
        "faq.FaqPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Give FAQ Page"),
    )
    giving_faq_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the giving faq section of the page"),
    )
    giving_faq_image_alt_text = models.CharField(
        _("Giving FAQ Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the giving faq image"),
    )
    # translatable buttons section for Give Page
    give_to_missionary_button = models.CharField(
        _("Give to a Missionary Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Give to a Missionary button"),
    )
    executive_initiatives_button = models.CharField(
        _("Executive Initiatives Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Executive Initiatives button"),
    )
    list_of_missionary_button = models.CharField(
        _("List of Missionaries Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for List of Missionaries button"),
    )
    giving_initiatives_slider_view_all_button = models.CharField(
        _("View All Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for View All button"),
    )
    giving_initiatives_slider_give_now_button = models.CharField(
        _("Give Now Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Give Now button"),
    )
    giving_initiatives_slider_learn_more_button = models.CharField(
        _("Learn More Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Learn More button"),
    )
    disaster_relief_slider_give_now_button = models.CharField(
        _("Give Now Button Text in Disaster Relief Section"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Give Now button"),
    )
    disaster_relief_slider_learn_more_button = models.CharField(
        _("Learn More Button Text in Disaster Relief Section"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Learn More button"),
    )
    legacy_giving_button = models.CharField(
        _("Legacy Giving Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Legacy Giving button"),
    )
    giving_faq_button = models.CharField(
        _("Giving FAQ Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for Giving FAQ button"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                FieldPanel("header_side_text"),
                FieldPanel("header_title_text"),
                FieldPanel("header_title_description"),
                PageChooserPanel("missionary_page"),
            ],
            heading=_("Header Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("first_section_image"),
                FieldPanel("first_section_image_alt_text"),
                FieldPanel("first_section_title"),
            ],
            heading=_("First Section"),
        ),
        MultiFieldPanel(
            [
                PageChooserPanel("special_give_index_page"),
                ImageChooserPanel("initiatives_background_image"),
                FieldPanel("initiatives_background_image_alt_text"),
                FieldPanel("slider_header_text"),
            ],
            heading=_("Initiatives Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("second_section_image"),
                FieldPanel("second_section_image_alt_text"),
                PageChooserPanel("second_section_dedicated_page"),
            ],
            heading=_("Second Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("is_legacy_page_external"),
                FieldPanel("legacy_giving_external_url"),
                PageChooserPanel("legacy_giving_page"),
                ImageChooserPanel("legacy_giving_image"),
                FieldPanel("legacy_giving_image_alt_text"),
                PageChooserPanel("giving_faq_page"),
                ImageChooserPanel("giving_faq_image"),
                FieldPanel("giving_faq_image_alt_text"),
            ],
            heading=_("Other Fields"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("give_to_missionary_button"),
                FieldPanel("executive_initiatives_button"),
                FieldPanel("list_of_missionary_button"),
                FieldPanel("giving_initiatives_slider_view_all_button"),
                FieldPanel("giving_initiatives_slider_give_now_button"),
                FieldPanel("giving_initiatives_slider_learn_more_button"),
                FieldPanel("disaster_relief_slider_give_now_button"),
                FieldPanel("disaster_relief_slider_learn_more_button"),
                FieldPanel("legacy_giving_button"),
                FieldPanel("giving_faq_button"),
            ],
            heading=_("Translatable Give page buttons and text fields"),
        ),
    ]
    additional_search_fields = [
        index.SearchField("header_side_text", partial_match=True),
        index.SearchField("header_title_text", partial_match=True),
        index.SearchField("header_title_description", partial_match=True),
        index.SearchField("first_section_title", partial_match=True),
        index.SearchField("initiatives_title", partial_match=True),
        index.SearchField("initiatives_content", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields
