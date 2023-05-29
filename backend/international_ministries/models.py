from coreapi import Field
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class IndividualMinistryPage(Page):
    """Page for an Individual Ministry"""

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
        help_text=_("Alt text for the header image of the ministry"),
    )
    ministry_website = models.CharField(
        _("Ministry Website"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Website link for the individual ministry"),
    )
    first_section_header = models.CharField(
        _("First Section Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text that will be shown in the section below the header"),
    )
    first_section_content = RichTextField(
        _("First Section Content"),
        null=True,
        blank=True,
        help_text=_("Content text that will be shown in the section below the header"),
    )
    middle_section_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that is going to be displayed in the middle section of the page"
        ),
    )
    middle_section_image_alt_text = models.CharField(
        _("Middle Section Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the middle section image of the page"),
    )
    description_header = models.CharField(
        _("Description Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header of the description section of the page"),
    )
    description = RichTextField(
        _("description"),
        null=True,
        blank=True,
        help_text=_("Description section of the page"),
    )
    give_page_url = models.TextField(
        _("Give Page URL"),
        null=True,
        blank=True,
        help_text=_("URL of the give page for this specific individual ministry"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("ministry_website"),
        FieldPanel("first_section_header"),
        FieldPanel("first_section_content"),
        ImageChooserPanel("middle_section_image"),
        FieldPanel("middle_section_image_alt_text"),
        FieldPanel("description_header"),
        FieldPanel("description"),
        FieldPanel("give_page_url"),
    ]

    additional_search_fields = [
        index.SearchField("first_section_header", partial_match=True),
        index.SearchField("first_section_content", partial_match=True),
        index.SearchField("description_header", partial_match=True),
        index.SearchField("description", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class InternationalMinistriesPage(Page):
    """Page for international ministries"""

    header_sub_title = models.CharField(
        _("Header Sub-title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown underneath of the title of the page"),
    )
    header_bottom_text = models.CharField(
        _("Header Bottom Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shwon at the bottom of the header portion of the page"
        ),
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
    header_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Header background image that is going to be displayed for the page"
        ),
    )
    header_background_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header background image of the page"),
    )
    header_map_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Header map image that is going to be displayed for the page"),
    )
    header_map_image_alt_text = models.CharField(
        _("Header Map Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header map image of the page"),
    )
    header_join_the_team_button_text = models.CharField(
        _("Join the team button text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set the text for Join the team button"),
    )
    header_join_the_team_button_url = models.CharField(
        _("Join the team button url"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set the URL for Join the team button"),
    )
    description_header = models.CharField(
        _("Description Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header of the description section of the page"),
    )
    description = RichTextField(
        _("description"),
        null=True,
        blank=True,
        help_text=_("Description section of the page"),
    )
    stories_section = models.ForeignKey(
        "stories.StoryIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Stories section of the page"),
        verbose_name=_("Stories Section"),
    )
    areas_of_ministries_header = models.CharField(
        _("Areas of Ministries Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown as the header of the areas of ministries section of the page"
        ),
    )
    individual_ministries_readmore_button_text = models.CharField(
        _("Read More Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Read more button text at the end of each individual ministries in areas of ministries section."
        ),
    )
    giving_initiative_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background image that is going to be displayed for giving initiative section of the page"
        ),
    )
    giving_initiative_background_image_alt_text = models.CharField(
        _("Giving Initiative Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Alt text for the background image that is going to be displayed for giving initiative section of the page"
        ),
    )
    giving_initiative_title = models.CharField(
        _("Giving Initiative Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("The title for the giving initiative section"),
    )
    giving_initiative_body = models.TextField(
        _("Giving Initiative Body"),
        null=True,
        blank=True,
        help_text=_("The text that will be shown under the giving initiative title"),
    )
    start_your_gift_today_button_text = models.CharField(
        _("Start Your Gift Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the start your gift today button in the giving initiative section."),
    )
    director_text = models.CharField(
        _("Director Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("The text above the directors name."),
    )
    director_name = models.CharField(
        _("Director Name"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("The name of the director for the region"),
    )
    director_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image of the director for the region"),
    )
    director_image_alt_text = models.CharField(
        _("Director Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the director image"),
    )
    related_ministries_links_text = models.CharField(
        _("Related Ministries Link Text"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Related ministries link text inside the directors section."),
    )
    director_phone_number = models.CharField(
        _("Director Phone Number"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The phone number of the director for the region"),
    )
    director_phone_text = models.CharField(
        _("Director Phone Text"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The phone text beside the directors phone number."),
    )
    director_website_link = models.CharField(
        _("Director Website Link"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The website link of the director"),
    )
    director_facebook_link = models.CharField(
        _("Director Facebook Link"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The Facebook link of the director"),
    )
    individual_ministries = models.ForeignKey(
        "international_ministries.IndividualMinistryPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Individual minitries section of the page"),
        verbose_name=_("Individual Ministries"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("header_sub_title"),
        FieldPanel("header_bottom_text"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("header_join_the_team_button_text"),
        FieldPanel("header_join_the_team_button_url"),
        ImageChooserPanel("header_background_image"),
        FieldPanel("header_background_image_alt_text"),
        ImageChooserPanel("header_map_image"),
        FieldPanel("header_map_image_alt_text"),
        FieldPanel("description_header"),
        FieldPanel("description"),
        PageChooserPanel("stories_section"),
        FieldPanel("areas_of_ministries_header"),
        FieldPanel("individual_ministries_readmore_button_text"),
        ImageChooserPanel("giving_initiative_background_image"),
        FieldPanel("giving_initiative_background_image_alt_text"),
        FieldPanel("giving_initiative_title"),
        FieldPanel("giving_initiative_body"),
        FieldPanel("start_your_gift_today_button_text"),
        FieldPanel("director_name"),
        FieldPanel("director_text"),
        ImageChooserPanel("director_image"),
        FieldPanel("director_image_alt_text"),
        FieldPanel("related_ministries_links_text"),
        FieldPanel("director_phone_text"),
        FieldPanel("director_phone_number"),
        FieldPanel("director_website_link"),
        FieldPanel("director_facebook_link"),
    ]

    subpage_types = ["IndividualMinistryPage"]
    additional_search_fields = [
        index.SearchField("header_sub_title", partial_match=True),
        index.SearchField("header_bottom_text", partial_match=True),
        index.SearchField("description_header", partial_match=True),
        index.SearchField("description", partial_match=True),
        index.SearchField("areas_of_ministries_header", partial_match=True),
        index.SearchField("giving_initiative_title", partial_match=True),
        index.SearchField("giving_initiative_body", partial_match=True),
        index.SearchField("director_name", partial_match=True),
        index.SearchField("director_phone_number", partial_match=True),
        index.SearchField("director_website_link", partial_match=True),
        index.SearchField("director_facebook_link", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    def children(self):
        return self.get_children().specific().live()
