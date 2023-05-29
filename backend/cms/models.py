from modelcluster.fields import ParentalKey

from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    FieldPanel,
    InlinePanel,
    ObjectList,
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from home.utils import get_upload_path


# Pages
class HomePage(Page):
    """Home page model"""

    template = "cms/home_page.html"

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
    header_section_missions_text = models.CharField(
        _("Header Section Missions Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the missions text for the header section"),
    )
    initial_subheader_section_missions_text = models.CharField(
        _("Initial Subheader Section Mission Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the initial subheader text under the missions header."),
    )
    subheader_section_missions_text = models.CharField(
        _("Subheader Section Mission Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the subheader text under the missions header."),
    )
    story_section = models.ForeignKey(
        "stories.StoryIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Story section of the page"),
        verbose_name=_("Story Section"),
    )
    region_section = models.ForeignKey(
        "regions.RegionIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Region section of the page"),
        verbose_name=_("Region Section"),
    )
    greg_mundis_section = models.ForeignKey(
        "cms.GregMundisInitiative",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Greg Mundis section of the page"),
        verbose_name=_("Greg Mundis Section"),
    )
    show_prayer_section = models.BooleanField(
        _("Show Prayer Section"),
        default=True,
        help_text=_(
            "Determines whether the prayer section will be shown in the home page"
        ),
    )
    prayer_section_background_color = models.CharField(
        _("Prayer Section Background Color"),
        null=True,
        blank=True,
        max_length=255,
        help_text=_(
            "Hex Code Color that will be shown in the prayer section. Example: #8155BA"
        ),
    )
    prayer_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the prayer section in the home page"),
        verbose_name=_("Prayer Image"),
    )
    prayer_image_alt_text = models.CharField(
        _("Prayer Image Alt Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            "Alt text for the image that will be shwon for the prayer section in the home page"
        ),
    )
    prayer_title = models.CharField(
        _("Prayer Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title of the prayer that will be shown in the prayer section"),
    )
    prayer_body = models.TextField(
        _("Prayer Body"),
        null=True,
        blank=True,
        help_text=_("Body of the prayer that will be shown in the prayer section"),
    )
    prayer_button_one = models.CharField(
        _("Prayer Button One"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Prayer button text in the prayer section"),
    )
    prayer_button_two = models.CharField(
        _("Prayer Button Two"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Prayer button text in the prayer section"),
    )
    prayer_button_one_url = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the URL for Prayer button one in the prayer section"),
    )
    prayer_button_two_url = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the URL for Prayer button two in the prayer section"),
    )
    pray_page = models.ForeignKey(
        "prayers.PrayerPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Prayer page"),
        verbose_name=_("Prayer Page"),
    )
    give_page = models.ForeignKey(
        "give.GivePage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Give page"),
        verbose_name=_("Give Page"),
    )
    go_page = models.ForeignKey(
        "go.GoPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Go page"),
        verbose_name=_("Go Page"),
    )
    greg_mundis_section_top_text = models.CharField(
        _("Greg Mundis Section Top Text"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Set the top text for the Greg Mundis section in the home page"),
    )
    greg_mundis_section_bottom_text = models.CharField(
        _("Greg Mundis Section Bottom Text"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Set the bottom text for the Greg Mundis section in the home page"),
    )
    greg_mundis_section_thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Thumbnail image that is going to be displayed for the video in Greg Mundis Section."),
    )

    # Nav buttons
    are_you_called_button_nav = models.CharField(
        _("Are you Called button text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Are you called button text in the navbar section"),
    )

    # Menu modal buttons
    resources_tab_button = models.CharField(
        _("Resources tab text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Resources tab text in the menu modal"),
    )
    explore_tab_button = models.CharField(
        _("Explore tab text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Explore tab text in the menu modal"),
    )
    strategy_tab_button = models.CharField(
        _("Strategy tab text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Resources tab text in the menu modal"),
    )
    pray_modal_button = models.CharField(
        _("Pray button modal text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Pray button text in the menu modal"),
    )
    give_modal_button = models.CharField(
        _("Give button modal text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Give button text in the menu modal"),
    )
    go_modal_button = models.CharField(
        _("Go button modal text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Go button text in the menu modal"),
    )
    all_resources_modal_button = models.CharField(
        _("All Resources button text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set All resources button text in the menu modal"),
    )

    # Header section buttons home page
    pray_button = models.CharField(
        _("Pray button text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Pray button text in the home page"),
    )
    give_button = models.CharField(
        _("Give button text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Give button text in the home page"),
    )
    go_button = models.CharField(
        _("Go button text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Go button text in the home page"),
    )

    # Regions slider section
    region_section_header_text = models.CharField(
        _("Region Section Header Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the Region section header text in the home page"),
    )
    region_section_map_view_text = models.CharField(
        _("Region Section Map View Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the Region section map view text in the home page"),
    )
    region_section_explore_button = models.CharField(
        _("Region Section Explore Button"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the Region section explore button in the home page"),
    )

    # Missions section
    mission_section_header_title = models.CharField(
        _("Mission section header title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set mission section header title in the home page"),
    )

    # Notifications settings
    email_button_pill_text = models.CharField(
        _("Email Button Pill text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Email Button Pill text in notifications settings modal"),
    )
    quick_pages_text = models.CharField(
        _("Quick Pages section text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set quick pages text in notifications settings modal"),
    )
    notification_settings_column_text = models.CharField(
        _("Notification Settings column text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set notification settings column text in notifications settings modal"
        ),
    )
    notification_settings_side_text = models.CharField(
        _("Notification Settings side text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set notification settings side text in notifications settings modal"
        ),
    )
    prayer_notification_header_text = models.CharField(
        _("Prayer Notification Header text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set Prayer Notification Header text in notifications settings modal"
        ),
    )
    prayer_notification_sub_text = models.CharField(
        _("Prayer Notification Sub text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set Prayer Notification Sub text in notifications settings modal"),
    )
    giving_initiatives_notification_header_text = models.CharField(
        _("Giving Initiatives Notification Header text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set Giving Initiatives Notification Header text in notifications settings modal"
        ),
    )
    giving_initiatives_notification_sub_text = models.CharField(
        _("Giving Initiatives Notification Sub text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set Giving Initiatives Notification Sub text in notifications settings modal"
        ),
    )
    stories_notification_header_text = models.CharField(
        _("Stories Notification Header text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set Stories Notification Header text in notifications settings modal"
        ),
    )
    stories_notification_sub_text = models.CharField(
        _("Stories Notification Sub text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set Stories Notification Sub text in notifications settings modal"
        ),
    )
    # Search Page Translations
    search_result_page_input_placeholder = models.CharField(
        _("Search Result Page Input Placeholder"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set placeholder text for search input in search result page."
        ),
    )
    search_result_page_search_button_text = models.CharField(
        _("Search Result Page Search Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set search button text text in search result page."
        ),
    )
    search_result_page_search_result_for_text = models.CharField(
        _("Search Result Page Search Result For Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set search result for text text in search result page."
        ),
    )
    search_result_page_no_result_found_text = models.CharField(
        _("Search Result Page No Result Found Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text displayed when there are no matching query results."
        ),
    )
    search_result_page_empty_query_text = models.CharField(
        _("Search Result Page Empty Query Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set search result for text text in search result page."
        ),
    )
    login_modal_header = models.CharField(
        _("Login Modal Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Set the text of the login modal header"
        ),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("header_section_missions_text"),
        FieldPanel("initial_subheader_section_missions_text"),
        FieldPanel("subheader_section_missions_text"),
        FieldPanel("login_modal_header"),
        InlinePanel(
            "home_page_rotate_texts",
            heading="Header section for rotating text",
            label="Header section rotating text",
        ),
        InlinePanel(
            "home_page_images",
            heading="Home Page Header Background Images",
            label="Home Page Background Images",
        ),
        PageChooserPanel("pray_page"),
        PageChooserPanel("give_page"),
        PageChooserPanel("go_page"),
        PageChooserPanel("story_section"),
        PageChooserPanel("region_section"),
        PageChooserPanel("greg_mundis_section"),
        FieldPanel("show_prayer_section"),
        FieldPanel("prayer_section_background_color"),
        FieldPanel("prayer_title"),
        FieldPanel("prayer_body"),
        FieldPanel("prayer_button_one"),
        FieldPanel("prayer_button_two"),
        FieldPanel("prayer_button_one_url"),
        FieldPanel("prayer_button_two_url"),
        FieldPanel("prayer_image_alt_text"),
        FieldPanel("greg_mundis_section_top_text"),
        FieldPanel("greg_mundis_section_bottom_text"),
        ImageChooserPanel("greg_mundis_section_thumbnail_image"),
        ImageChooserPanel("prayer_image"),
        MultiFieldPanel(
            [
                FieldPanel("email_button_pill_text"),
                FieldPanel("quick_pages_text"),
                FieldPanel("notification_settings_column_text"),
                FieldPanel("notification_settings_side_text"),
                FieldPanel("prayer_notification_header_text"),
                FieldPanel("prayer_notification_sub_text"),
                FieldPanel("giving_initiatives_notification_header_text"),
                FieldPanel("giving_initiatives_notification_sub_text"),
                FieldPanel("stories_notification_header_text"),
                FieldPanel("stories_notification_sub_text"),
            ],
            heading="Translatable Notifications Settings Modal buttons and text fields",
        ),
        MultiFieldPanel(
            [
                FieldPanel("mission_section_header_title"),
                FieldPanel("are_you_called_button_nav"),
                FieldPanel("resources_tab_button"),
                FieldPanel("explore_tab_button"),
                FieldPanel("strategy_tab_button"),
                FieldPanel("pray_modal_button"),
                FieldPanel("give_modal_button"),
                FieldPanel("go_modal_button"),
                FieldPanel("all_resources_modal_button"),
                FieldPanel("pray_button"),
                FieldPanel("give_button"),
                FieldPanel("go_button"),
                FieldPanel("region_section_header_text"),
                FieldPanel("region_section_map_view_text"),
                FieldPanel("region_section_explore_button"),
            ],
            heading="Translatable Home Page buttons and text fields",
        ),
        MultiFieldPanel(
            [
                FieldPanel("search_result_page_input_placeholder"),
                FieldPanel("search_result_page_search_button_text"),
                FieldPanel("search_result_page_search_result_for_text"),
                FieldPanel("search_result_page_no_result_found_text"),
                FieldPanel("search_result_page_empty_query_text"),

            ],
            heading="Translatable Search Page Buttons and Text Fields",
        ),
    ]
    additional_search_fields = [
        index.SearchField("prayer_title", partial_match=True),
        index.SearchField("prayer_body", partial_match=True),
        index.SearchField("header_section_missions_text", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class GregMundisInitiative(Page):
    """Greg Mundis and Initiatives Page"""

    # Header Section
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

    # Message Section
    message_heading = models.CharField(
        _("Message Heading"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Message Heading for the page"),
    )
    message_body = models.TextField(
        _("Message Body"),
        blank=True,
        null=True,
        help_text=_("Body for the heading of the page"),
    )
    message_video_embed_url = models.CharField(
        _("Message Video Embed URL"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(
            "This needs to be the embed URL of the video or else the video player will not work"
        ),
    )

    # Greg Mundis Section
    greg_mundis_name = models.CharField(
        _("Greg Mundis Name"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("Name of Greg Mundis displayed"),
    )

    greg_mundis_position = models.CharField(
        _("Greg Mundis Position"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("Title of Greg Mundis displayed"),
    )
    greg_mundis_company = models.CharField(
        _("Greg Mundis Company"),
        max_length=50,
        blank=True,
        null=True,
        help_text="Company of Greg Mundis displayed",
    )

    greg_mundis_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("Greg Mundis Image"),
        help_text=_("Greg Mundis Image"),
    )

    greg_mundis_image_alt_text = models.CharField(
        _("Greg Mundis Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the image of greg mundis"),
    )

    greg_mundis_description = RichTextField(
        _("Greg Mundis Description"),
        null=True,
        blank=True,
        help_text=_("Description under Greg Mundis name and title"),
    )
    # Executive slider section
    executive_priorities_title = models.CharField(
        _("Executive Priorities Title"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set text for the Executive Priorities Title"),
    )
    executive_read_all_button = models.CharField(
        _("Read All Button Text"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set text for the Read All button"),
    )

    # Contact Info section
    contact_info_title = models.CharField(
        _("Contact Info Title"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Contact Info Title"),
    )

    # Contact Information body section
    contact_info_company_name = models.CharField(
        _("Company Name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Company name to be displayed in the page"),
    )
    contact_info_address1 = models.CharField(
        _("Address 1"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("First line of the company address to be displayed in the page"),
    )
    contact_info_address2 = models.CharField(
        _("Address 2"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Second line of the company address to be displayed in the page"),
    )
    contact_info_phone_number = models.CharField(
        _("Phone Number"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Phone number to be displayed in the page"),
    )

    contact_info_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name="+",
        help_text=_("Background image of the contact information "),
    )

    contact_info_background_image_alt_text = models.CharField(
        _("Background Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the background image of the contact information"),
    )

    # Contact Person section

    contact_person_name = models.CharField(
        _("Name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Name of the contact person"),
    )
    contact_person_email_address = models.EmailField(
        _("Email Address"),
        blank=True,
        max_length=254,
        help_text=_("Email address of the contact person"),
    )
    contact_person_position = models.CharField(
        _("Position"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Position of the person in the company"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                ImageChooserPanel("thumbnail_image"),
                FieldPanel("thumbnail_image_alt_text"),
                FieldPanel("message_heading"),
                FieldPanel("message_body"),
                FieldPanel("message_video_embed_url"),
            ],
            heading="Header Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("greg_mundis_name"),
                FieldPanel("greg_mundis_position"),
                FieldPanel("greg_mundis_company"),
                ImageChooserPanel("greg_mundis_image"),
                FieldPanel("greg_mundis_description"),
            ],
            heading="Greg Mundis Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("executive_priorities_title"),
                FieldPanel("executive_read_all_button"),
            ],
            heading="Executive Priorities Section",
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("contact_info_background_image"),
                FieldPanel("contact_info_title"),
                FieldPanel("contact_info_background_image_alt_text"),
                FieldPanel("contact_info_company_name"),
                FieldPanel("contact_info_address1"),
                FieldPanel("contact_info_address2"),
                FieldPanel("contact_info_phone_number"),
            ],
            heading="Contact Information Section",
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "contact_persons",
                    label=_("Contact Person"),
                    panels=None,
                ),
            ],
            heading="Contact Person Section",
        ),
    ]
    additional_search_fields = [
        index.SearchField("message_heading", partial_match=True),
        index.SearchField("message_body", partial_match=True),
        index.SearchField("greg_mundis_name", partial_match=True),
        index.SearchField("greg_mundis_position", partial_match=True),
        index.SearchField("greg_mundis_company", partial_match=True),
        index.SearchField("contact_info_company_name", partial_match=True),
        index.SearchField("contact_info_address1", partial_match=True),
        index.SearchField("contact_info_address2", partial_match=True),
        index.SearchField("contact_info_phone_number", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class ContactUsPage(Page):
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
    header_form_text = models.CharField(
        _("Header Form Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the header for the contact form"),
    )
    location_header_text = models.CharField(
        _("Location Header Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the location header text"),
    )
    location_sub_text = models.CharField(
        _("Location Sub Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the location sub text"),
    )
    contact_us_address_text1 = models.CharField(
        _("Address Text 1"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the address text"),
    )
    contact_us_address_text2 = models.CharField(
        _("Address Text 2"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the address text"),
    )
    contact_us_phone_number = models.CharField(
        _("Phone Number"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the phone number"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("header_form_text"),
        FieldPanel("location_header_text"),
        FieldPanel("location_sub_text"),
        FieldPanel("contact_us_address_text1"),
        FieldPanel("contact_us_address_text2"),
        FieldPanel("contact_us_phone_number"),
    ]


class ContactUsModel(models.Model):
    contact_us_first_name = models.CharField(
        _("First Name"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("First Name of the contact person"),
    )
    contact_us_last_name = models.CharField(
        _("Last Name"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Last Name of the contact person"),
    )
    contact_us_email = models.EmailField(
        _("Email Address"),
        blank=True,
        max_length=254,
        help_text=_("Email address of the contact person"),
    )
    contact_us_phone_number = models.CharField(
        _("Phone Number"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Phone number of the contact person"),
    )
    contact_us_church_name = models.CharField(
        _("Church Name"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Church name of the contact person"),
    )
    contact_us_comment_and_message = models.TextField(
        _("Comment and Message"),
        null=True,
        blank=True,
        help_text=_("Comment and message of the contact person"),
    )

    class Meta:
        verbose_name = _("Contact Us Form")
        verbose_name_plural = _("Contact Us Forms")

    def __str__(self):
        return f"{self.contact_us_last_name} form"


class MissionaryApi(ClusterableModel):
    """Missionary API for CAMs, Sending Districts, and Regions"""

    panels = [
        InlinePanel("cam_missionary_api", heading="CAMS", label="CAMS"),
        InlinePanel(
            "sending_district_missionary_api",
            heading="Sending Districts",
            label="Sending Districts",
        ),
        InlinePanel(
            "region_missionary_api",
            heading="Regions",
            label="Regions",
        ),
    ]


class SendingDistrict(Orderable):

    missionary_api = ParentalKey(
        "MissionaryApi",
        related_name="sending_district_missionary_api",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Sending Districts"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Name of the district"),
    )
    number = models.CharField(
        _("Number"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("Number of the district"),
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Sending District")
        verbose_name_plural = _("Sending Districts")


class Cam(Orderable):
    CAM_AREA = "Area"
    CAM_COUNTRY = "Country"
    CAM_MINISTRY = "Ministry"
    CAM_CHOICES = [
        (CAM_AREA, "Area"),
        (CAM_COUNTRY, "Country"),
        (CAM_MINISTRY, "Ministry"),
    ]

    missionary_api = ParentalKey(
        "MissionaryApi",
        related_name="cam_missionary_api",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("CAMS"),
    )

    text = models.CharField(
        _("Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Area, Country, or Ministry name to be displayed"),
    )

    value = models.CharField(
        _("Value"),
        max_length=100,
        null=True,
        blank=True,
        help_text=("Value of Area, Country, Ministry"),
    )

    type = models.CharField(
        _("Type"),
        choices=CAM_CHOICES,
        max_length=50,
        help_text=("Set the type as Area, Country, or Ministry"),
    )

    class Meta:
        verbose_name = _("CAM")
        verbose_name_plural = _("CAMS")

    def __str__(self):
        return f"{self.text} - {self.type}"


class ContactPerson(Orderable):
    page = ParentalKey(
        GregMundisInitiative,
        on_delete=models.CASCADE,
        null=True,
        related_name="contact_persons",
    )
    name = models.CharField(
        _("Name"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Name of the contact person"),
    )
    email_address = models.EmailField(
        _("Email Address"),
        blank=True,
        max_length=254,
        help_text=_("Email address of the contact person"),
    )
    position = models.CharField(
        _("Position"),
        max_length=50,
        null=True,
        blank=True,
        help_text=_("Position of the person in the company"),
    )


# Models
class Region(ClusterableModel):

    missionary_api = ParentalKey(
        "MissionaryApi",
        related_name="region_missionary_api",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Regions"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Name of the region"),
    )
    is_main_region = models.BooleanField(
        _("Is Main Region"),
        default=False,
        null=True,
        help_text=_("Set this as true"),
    )
    region_guid = models.CharField(
        _("Region GUID"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the RegionGUID"),
    )
    header_map_image = models.FileField(
        _("Header Map Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_(
            "Image that will be shown in the map portion in the header of the page"
        ),
    )
    header_map_image_alt_text = models.CharField(
        _("Header Map Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the map image in the header of the page"),
    )

    def __str__(self):
        return self.name

    panels = [
        FieldPanel("name"),
        FieldPanel("is_main_region"),
        FieldPanel("region_guid"),
        FieldPanel("header_map_image"),
        FieldPanel("header_map_image_alt_text"),
        InlinePanel(
            "region_images",
            heading="Missionary Region Image",
            label="Regions header image",
        ),
    ]

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class MissionaryRegionImage(Orderable):
    """Images for each region according to a missionary"""

    region = ParentalKey(
        "Region",
        related_name="region_images",
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Region"),
        help_text=_("Region assigned for the images"),
    )
    header_image = models.FileField(
        _("Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_(
            "Background image that will be shown in the header portion of the page"
        ),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )

    class Meta:
        verbose_name = _("Missionary Region Image")
        verbose_name_plural = _("Missionary Region Images")

    def __str__(self):
        return self.region.name


class SocialMedia(models.Model):
    """Model for Social Media account links"""

    facebook_url = models.CharField(
        _("Facebook URL"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Facebook URL link"),
    )
    vimeo_url = models.CharField(
        _("Vimeo URL"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Viemo URL link"),
    )
    youtube_url = models.CharField(
        _("Youtube URL"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Youtube URL link"),
    )
    instagram_url = models.CharField(
        _("Instagram URL"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Instagram URL link"),
    )

    class Meta:
        verbose_name = _("Social Media")
        verbose_name_plural = _("Social Media")

    def __str__(self):
        return "Social Media"


class MissionText(ClusterableModel):
    """Model for the text that will be shown besides the missions"""

    text = models.TextField(
        _("Text"),
        null=True,
        help_text=_("Text that will be shown besides the missions"),
    )
    text_es = models.TextField(
        _("Text in Spanish"),
        null=True,
        help_text=_("Text that will be shown besides the missions"),
    )
    our_mission_text = models.TextField(
        _("Our Mission Text"),
        null=True,
        help_text=_("Our mission text above missions section."),
    )
    our_mission_text_es = models.TextField(
        _("Our Mission Text in Spanish"),
        null=True,
        help_text=_("Our mission text above missions section."),
    )

    class Meta:
        verbose_name = _("RPTS Section")
        verbose_name_plural = _("RPTS Section")

    panels = [
        FieldPanel("our_mission_text"),
        FieldPanel("our_mission_text_es"),
        FieldPanel("text"),
        FieldPanel("text_es"),
        InlinePanel("mission_texts"),
    ]

    def __str__(self):
        return self.text


class Mission(Orderable):
    """Mission model that will be displayed on some of the pages"""

    mission_text = ParentalKey(
        "MissionText",
        related_name="mission_texts",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Set mission text for missions"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Name of the mission"),
    )
    name_es = models.CharField(
        _("Name in Spanish"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Name of the mission"),
    )
    image = models.ImageField(
        _("Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_("Image of the mission"),
    )
    description = models.TextField(
        _("Description"),
        null=True,
        blank=True,
        help_text=_("Description of the mission"),
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("name_es"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.name


class MenuResourcePage(models.Model):
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_(
            "Page that you want to show in the resources tab in the menu. This will also serve as the default page title that will be shown in the menu"
        ),
    )
    page_title = models.CharField(
        _("Page Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Name of the page that will be displayed if you dont want the page name to display in the menu."
        ),
    )
    page_title_es = models.CharField(
        _("Page Title in Spanish"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Name of the page that will be displayed in spanish if you dont want the page name to display in the menu."
        ),
    )
    is_external_page = models.BooleanField(
        _("Is External Page"),
        default=False,
        null=True,
        help_text=_(
            "Set this as true if the page youu want to add in the resource section is an external website/page"
        ),
    )
    external_page_url = models.TextField(
        _("External Page URL"),
        null=True,
        blank=True,
        help_text=_("URL of the external page you want to add"),
    )
    bottom_text = models.TextField(
        _("Bottom Text"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown at the bottom of the page title"),
    )
    bottom_text_es = models.TextField(
        _("Bottom Text in Spanish"),
        null=True,
        blank=True,
        help_text=_("Spanish text that will be shown at the bottom of the page title"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the page in the menu"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )

    class Meta:
        verbose_name = _("Menu Resource Page")
        verbose_name_plural = _("Menu Resource Pages")

    def __str__(self):
        return self.page_title if self.page_title else self.page.title

    custom_panels = [
        PageChooserPanel(
            "page",
        ),
        FieldPanel("page_title", classname="page_title"),
        FieldPanel("page_title_es", classname="page_title_es"),
        FieldPanel("is_external_page", classname="is_external_page"),
        FieldPanel("external_page_url", classname="external_page_url"),
        FieldPanel("bottom_text", classname="bottom_text"),
        FieldPanel("bottom_text_es", classname="bottom_text_es"),
        ImageChooserPanel("image"),
        FieldPanel("image_alt_text", classname="image_alt_text"),
    ]

    edit_handler = ObjectList(custom_panels)


class MenuExplorePage(models.Model):
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_(
            "Page that you want to show in the explore tab in the menu. This will also serve as the default page title that will be shown in the menu"
        ),
    )
    page_title = models.CharField(
        _("Page Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Name of the page that will be displayed if you dont want the page name to display in the menu."
        ),
    )
    page_title_es = models.CharField(
        _("Page Title in Spanish"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Name of the page that will be displayed in spanish if you dont want the page name to display in the menu."
        ),
    )
    bottom_text = models.TextField(
        _("Bottom Text"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown at the bottom of the page title"),
    )
    bottom_text_es = models.TextField(
        _("Bottom Text in Spanish"),
        null=True,
        blank=True,
        help_text=_("Spanish text that will be shown at the bottom of the page title"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the page in the menu"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )

    class Meta:
        verbose_name = _("Menu Explore Page")
        verbose_name_plural = _("Menu Explore Pages")

    def __str__(self):
        return self.page_title if self.page_title else self.page.title

    custom_panels = [
        PageChooserPanel(
            "page",
        ),
        FieldPanel("page_title", classname="page_title"),
        FieldPanel("page_title_es", classname="page_title_es"),
        FieldPanel("bottom_text", classname="bottom_text"),
        FieldPanel("bottom_text_es", classname="bottom_text_es"),
        ImageChooserPanel("image"),
        FieldPanel("image_alt_text", classname="image_alt_text"),
    ]

    edit_handler = ObjectList(custom_panels)


class MenuStrategyPage(models.Model):
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_(
            "Page that you want to show in the strategy tab in the menu. This will also serve as the default page title that will be shown in the menu"
        ),
    )
    bottom_text = models.TextField(
        _("Bottom Text"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown at the bottom of the page title"),
    )
    bottom_text_es = models.TextField(
        _("Bottom Text in Spanish"),
        null=True,
        blank=True,
        help_text=_("Spanish text that will be shown at the bottom of the page title"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the page in the menu"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )
    page_section_link = models.CharField(
        _("Page Section Link"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("name of the section you want to go to in the strategy page"),
    )

    class Meta:
        verbose_name = _("Menu Strategy Page")
        verbose_name_plural = _("Menu Strategy Page")

    def __str__(self):
        return self.bottom_text

    custom_panels = [
        PageChooserPanel(
            "page",
        ),
        FieldPanel("bottom_text", classname="bottom_text"),
        FieldPanel("bottom_text_es", classname="bottom_text_es"),
        ImageChooserPanel("image"),
        FieldPanel("image_alt_text", classname="image_alt_text"),
        FieldPanel("page_section_link", classname="page_section_link"),
    ]

    edit_handler = ObjectList(custom_panels)


class MarketingAutomationSystem(models.Model):
    header_tag_opening = models.TextField(
        _("AFTER opening <header> tag"),
        null=True,
        blank=True,
        help_text=_("Header Tag Opening"),
    )
    header_tag_closing = models.TextField(
        _("BEFORE closing <header> tag"),
        null=True,
        blank=True,
        help_text=_("Header Tag Closing"),
    )
    body_tag_opening = models.TextField(
        _("AFTER opening <body> tag"),
        null=True,
        blank=True,
        help_text=_("Body Tag Opening"),
    )
    body_tag_closing = models.TextField(
        _("BEFORE closing <body> tag"),
        null=True,
        blank=True,
        help_text=_("Body Tag Closing"),
    )
    contact_us = models.TextField(
        _("Contact Us Form"),
        null=True,
        blank=True,
        help_text=_("Set the form in the contact us page"),
    )
    bridge_the_gap_sign_up_subscription = models.TextField(
        _("Bridge The Gap Sign Up Subscription Form"),
        null=True,
        blank=True,
        help_text=_("Set the form in the bridge the gap section in prayers page"),
    )
    media_hub_register = models.TextField(
        _("Media Hub Register Form"),
        null=True,
        blank=True,
        help_text=_("Set the form for the media hub"),
    )
    media_hub_support_request = models.TextField(
        _("Media Hub Support Request Form"),
        null=True,
        blank=True,
        help_text=_("Set the form for the media hub support"),
    )

    class Meta:
        verbose_name = _("Marketing Automation System Page")
        verbose_name_plural = _("Marketing Automation System Pages")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("header_tag_opening"),
                FieldPanel("header_tag_closing"),
                FieldPanel("body_tag_opening"),
                FieldPanel("body_tag_closing"),
            ],
            heading=_("Marketing Automation Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("contact_us"),
                FieldPanel("bridge_the_gap_sign_up_subscription"),
                FieldPanel("media_hub_register"),
                FieldPanel("media_hub_support_request"),
            ],
            heading=_("Forms Section"),
        ),
    ]


class HomePageImages(Orderable):
    home_page = ParentalKey(
        "HomePage",
        related_name="home_page_images",
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Home Page Header Images"),
        help_text=_("Page assigned to images"),
    )
    header_image = models.FileField(
        _("Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_(
            "Background image that will be shown in the header portion of the page"
        ),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )


class HomePageMissionTextRotate(Orderable):
    home_page_rotate_text = ParentalKey(
        "HomePage",
        related_name="home_page_rotate_texts",
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("Home Page Rotate Text"),
        help_text=_("Text assigned to header section mission"),
    )
    header_section_rotate_text = models.TextField(
        _("Text"),
        null=True,
        help_text=_("Text that will rotate besides the Missions text"),
    )


class FooterSection(ClusterableModel):
    """
    Footer Section Editable buttons and URLs
    """

    panels = [
        MultiFieldPanel(
            [
                InlinePanel(
                    "footer_column_information",
                    heading="First Section",
                    label="First Section",
                ),
            ],
            heading=_("First Section"),
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "footer_column_home",
                    heading="Second section",
                    label="Second section",
                )
            ],
            heading=_("Second section"),
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "footer_column_resources",
                    heading="Third Section",
                    label="Third Section",
                )
            ],
            heading=_("Third Section"),
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "footer_column_explore",
                    heading="Fourth Section",
                    label="Fourth Section",
                )
            ],
            heading=_("Fourth Section"),
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "footer_column_strategy",
                    heading="Fifth Section",
                    label="Fifth Section",
                )
            ],
            heading=_("Fifth Section"),
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "footer_column_connect",
                    heading="Sixth Section",
                    label="Sixth Section",
                )
            ],
            heading=_("Sixth Section"),
        ),
    ]

    class Meta:
        verbose_name = _("Footer Section Button")
        verbose_name_plural = _("Footer Section Buttons")


class FooterInformationColumn(ClusterableModel):
    """
    Cluster where you can add fields that will show up in the Information column in the footer section
    """

    footer_column = ParentalKey(
        "FooterSection",
        related_name="footer_column_information",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Add first section column text/buttons here"),
    )
    header_image = models.FileField(
        _("Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_("Logo that will be shown in the first section of the footer"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Set the page that you want to link the field to"),
    )
    button_name = models.CharField(
        _(" Button Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the name of the button to be shown in the first section"),
    )
    address1 = models.CharField(
        _("Address 1"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Address 1 text in the footer section"),
    )
    address2 = models.CharField(
        _("Address 2"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Address 2 text in the footer section"),
    )
    phone_number = models.CharField(
        _("Phone Number"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Phone number in the footer section"),
    )
    copyright_text = models.CharField(
        _("Copyright text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Copyright text in the footer section"),
    )

    panels = [
        FieldPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        PageChooserPanel("page"),
        FieldPanel("button_name"),
        FieldPanel("address1"),
        FieldPanel("address2"),
        FieldPanel("phone_number"),
        FieldPanel("copyright_text"),
    ]

    class Meta:
        verbose_name = _("Footer First Column")
        verbose_name_plural = _("Footer First Column")


class FooterHomeColumn(ClusterableModel):
    """
    Cluster where you can add fields that will show up in the Information column in the footer section
    """

    footer_column = ParentalKey(
        "FooterSection",
        related_name="footer_column_home",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Add Home column buttons here"),
    )
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Set the page that you want to link the field to"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the name of the field to be shown in the home section"),
    )
    is_top_link = models.BooleanField(
        _("Is Top text"),
        default=False,
        null=True,
        help_text=_(
            "Set this to True to make text bold and moved at the top of the column"
        ),
    )

    def save(self, *args, **kwargs):
        top_link = super().save(*args, **kwargs)

        # Updates all other top links that are True to False
        if self.is_top_link:
            FooterHomeColumn.objects.exclude(id=self.id).update(is_top_link=False)

        return top_link

    panels = [
        PageChooserPanel("page"),
        FieldPanel("name"),
        FieldPanel("is_top_link"),
    ]

    class Meta:
        verbose_name = _("Footer Second Column")
        verbose_name_plural = _("Footer Second Column")


class FooterResourcesColumn(ClusterableModel):
    """
    Cluster where you can add fields that will show up in the Resources column in the footer section
    """

    footer_column = ParentalKey(
        "FooterSection",
        related_name="footer_column_resources",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Add Resources column buttons here"),
    )
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Set the page that you want to link the field to"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the name of the field to be shown in the resources section"),
    )
    is_top_link = models.BooleanField(
        _("Is Top text"),
        default=False,
        null=True,
        help_text=_(
            "Check the box to set this to True and make text bold and moved at the top of the column"
        ),
    )

    def save(self, *args, **kwargs):
        top_link = super().save(*args, **kwargs)

        # Updates all other top links that are True to False
        if self.is_top_link:
            FooterResourcesColumn.objects.exclude(id=self.id).update(is_top_link=False)

        return top_link

    panels = [
        PageChooserPanel("page"),
        FieldPanel("name"),
        FieldPanel("is_top_link"),
    ]

    class Meta:
        verbose_name = _("Footer Third Column")
        verbose_name_plural = _("Footer Third Column")


class FooterExploreColumn(ClusterableModel):
    """
    Cluster where you can add fields that will show up in the Explore column in the footer section
    """

    footer_column = ParentalKey(
        "FooterSection",
        related_name="footer_column_explore",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Add Explore column buttons here"),
    )
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Set the page that you want to link the field to"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the name of the field to be shown in the explore section"),
    )
    is_top_link = models.BooleanField(
        _("Is Top text"),
        default=False,
        null=True,
        help_text=_(
            "Check the box to set this to True and make text bold and moved at the top of the column"
        ),
    )

    def save(self, *args, **kwargs):
        top_link = super().save(*args, **kwargs)

        # Updates all other top links that are True to False
        if self.is_top_link:
            FooterExploreColumn.objects.exclude(id=self.id).update(is_top_link=False)

        return top_link

    panels = [
        PageChooserPanel("page"),
        FieldPanel("name"),
        FieldPanel("is_top_link"),
    ]

    class Meta:
        verbose_name = _("Footer Fourth Column")
        verbose_name_plural = _("Footer Fourth Column")


class FooterStrategyColumn(ClusterableModel):
    """
    Cluster where you can add fields that will show up in the Strategy column in the footer section
    """

    footer_column = ParentalKey(
        "FooterSection",
        related_name="footer_column_strategy",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Add Strategy column buttons here"),
    )
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Set the page that you want to link the field to"),
    )
    name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the name of the field to be shown in the strategy section"),
    )
    is_top_link = models.BooleanField(
        _("Is Top text"),
        default=False,
        null=True,
        help_text=_(
            "Check the box to set this to True and make text bold and moved at the top of the column"
        ),
    )

    def save(self, *args, **kwargs):
        top_link = super().save(*args, **kwargs)

        # Updates all other top links that are True to False
        if self.is_top_link:
            FooterStrategyColumn.objects.exclude(id=self.id).update(is_top_link=False)

        return top_link

    panels = [
        PageChooserPanel("page"),
        FieldPanel("name"),
        FieldPanel("is_top_link"),
    ]

    class Meta:
        verbose_name = _("Footer Fifth Column")
        verbose_name_plural = _("Footer Fifth Column")


class FooterConnectColumn(ClusterableModel):
    """
    Cluster where you can add fields that will show up in the sixth column in the footer section
    """

    footer_column = ParentalKey(
        "FooterSection",
        related_name="footer_column_connect",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text=_("Add Connect column buttons here"),
    )
    page = models.ForeignKey(
        "wagtailcore.Page",
        related_name="+",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Set the page that you want to link the field to"),
    )
    top_name = models.CharField(
        _("Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the top name to be shown in the sixth section"),
    )
    button_name = models.CharField(
        _("Button Name"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Set the name of the button to be shown in the sixth section"),
    )
    facebook_header_image = models.FileField(
        _("Facebook Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_(
            "Facebook logo that will be shown in the sixth section of the footer"
        ),
    )
    facebook_header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the facebook header image"),
    )
    vimeo_header_image = models.FileField(
        _("Vimeo Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_("Vimeo logo that will be shown in the sixth section of the footer"),
    )
    vimeo_header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Vimeo header image"),
    )
    youtube_header_image = models.FileField(
        _("Youtube Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_(
            "Youtube logo that will be shown in the sixth section of the footer"
        ),
    )
    youtube_header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the youtube header image"),
    )
    instagram_header_image = models.FileField(
        _("Instagram Header Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_(
            "Instagram logo that will be shown in the sixth section of the footer"
        ),
    )
    instagram_header_image_alt_text = models.CharField(
        _("Instagram Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Instagram header image"),
    )
    is_top_link = models.BooleanField(
        _("Is Top text"),
        default=False,
        null=True,
        help_text=_(
            "Check the box to set this to True and make text bold and moved at the top of the column"
        ),
    )

    def save(self, *args, **kwargs):
        top_link = super().save(*args, **kwargs)

        # Updates all other top links that are True to False
        if self.is_top_link:
            FooterStrategyColumn.objects.exclude(id=self.id).update(is_top_link=False)

        return top_link

    panels = [
        PageChooserPanel("page"),
        FieldPanel("is_top_link"),
        FieldPanel("top_name"),
        FieldPanel("button_name"),
        FieldPanel("facebook_header_image"),
        FieldPanel("facebook_header_image_alt_text"),
        FieldPanel("vimeo_header_image"),
        FieldPanel("vimeo_header_image_alt_text"),
        FieldPanel("youtube_header_image"),
        FieldPanel("youtube_header_image_alt_text"),
        FieldPanel("instagram_header_image"),
        FieldPanel("instagram_header_image_alt_text"),
    ]

    class Meta:
        verbose_name = _("Footer Sixth Column")
        verbose_name_plural = _("Footer Sixth Column")
