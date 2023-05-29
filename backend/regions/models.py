from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RegionPage(Page):
    """Page for a specific region"""

    region_page = models.ForeignKey(
        "RegionIndexPage",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    header_sub_text = models.TextField(
        _("Header Sub-text"),
        blank=True,
        null=True,
        help_text=_(
            "Text at the bottom of the name of the region in the header portion of the region page"
        ),
    )
    header_bottom_text = models.TextField(
        _("Header Bottom Text"),
        blank=True,
        null=True,
        help_text=_("Text at the bottom area of the header portion of the region page"),
    )
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown in the header portion of the region page"
        ),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    header_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown in the background of the header portion of the region page"
        ),
    )
    header_background_image_alt_text = models.CharField(
        _("Header Background Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the header background image"),
    )
    header_map_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown in the map portion in the header of the region page"
        ),
    )
    header_map_image_alt_text = models.CharField(
        _("Header Map Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the map image in the header of the region page"),
    )
    header_join_the_team_button_url = models.CharField(
        _("Join the team button url"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set the URL for Join the team button"),
    )
    stories_section = models.ForeignKey(
        "stories.StoryIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Story section of the page"),
        verbose_name=_("Story Section"),
    )

    giving_initiative_title = models.CharField(
        _("Giving Initiative Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("The title for the giving initiative section for the region page"),
    )
    giving_initiative_body = models.TextField(
        _("Giving Initiative Body"),
        null=True,
        blank=True,
        help_text=_(
            "The body part for the giving initiative section for the region page"
        ),
    )
    giving_initiative_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background image that will be shown in the giving initiative portion of the region page"
        ),
    )
    giving_initiative_background_image_alt_text = models.CharField(
        _("Giving Initiative Background Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_(
            "Alt text for the background image in the giving initiative portion of the region page"
        ),
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

    director_phone_number = models.CharField(
        _("Director Phone Number"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The phone number of the director for the region"),
    )

    region_website_link = models.CharField(
        _("Region Website Link"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The website link for the region"),
    )

    region_facebook_link = models.CharField(
        _("Region Facebook Link"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The facebook link for the region"),
    )

    population_number = models.CharField(
        _("Population Number"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("The website link for the region"),
    )

    spiritualy_lost = models.CharField(
        _("Spiritualy Lost"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Number of spiritualy lost people"),
    )

    unreached_people_groups = models.CharField(
        _("Unreached People Groups"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Number of unreached people groups"),
    )

    ag_constituents = models.CharField(
        _("AG Constituents"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Number of AG Constituents"),
    )

    ag_churches = models.CharField(
        _("AG Churches"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Number of ag churches"),
    )

    ag_ministers = models.CharField(
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Number of ag ministers"),
    )

    missionaries_and_associates = models.CharField(
        _("Missionaries and Associates"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Number of missionaries and associates"),
    )
    join_the_team_button = models.CharField(
        _("Join the Team Button"),
        max_length=225,
        null=True,
        blank=True,
        help_text=_("Set text for Join the Team Button"),
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
    giving_initiative_header_title = models.CharField(
        _("Giving Initiative Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Giving Initiative Header Title"),
    )
    start_your_gift_button = models.CharField(
        _("Start Your Gift Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Start Your Gift Button"),
    )
    director_header_title = models.CharField(
        _("Director Header Title Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Director Header Title"),
    )
    related_ministries_links_text = models.CharField(
        _("Related Ministries Links Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Related Ministries Links"),
    )
    phone_number_text = models.CharField(
        _("Phone Number Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Phone Number"),
    )
    view_button = models.CharField(
        _("View Text in Regional Web Site"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for View Text in Regional Web Site"),
    )
    regional_web_site_button = models.CharField(
        _("Regional Web Site Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Regional Web Site"),
    )
    population_section_title = models.CharField(
        _("Population Section Title Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Population Section Title"),
    )
    spiritually_lost_card_text = models.CharField(
        _("Spiritually Lost Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Spiritually Lost Card"),
    )
    unreached_people_groups_card_text = models.CharField(
        _("Unreached People Groups Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Unreached People Groups Card"),
    )
    ag_constituents_card_text = models.CharField(
        _("AG Constituents Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for AG Constituents Card"),
    )
    ag_churches_card_text = models.CharField(
        _("AG Churches Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for AG Churches Card"),
    )
    ag_ministers_card_text = models.CharField(
        _("AG Ministers Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for AG Ministers Card"),
    )
    missionaries_and_associates_card_text = models.CharField(
        _("Missionaries and Associates Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set text for Missionaries and Associates Card"),
    )
    region_slider_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Background Image for the region slider"),
    )
    region_slider_image_alt_text = models.CharField(
        _("Region Slider Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the region slider image"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("header_sub_text"),
                FieldPanel("header_bottom_text"),
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                ImageChooserPanel("header_background_image"),
                FieldPanel("header_background_image_alt_text"),
                ImageChooserPanel("header_map_image"),
                FieldPanel("header_map_image_alt_text"),
                FieldPanel("header_join_the_team_button_url"),
            ],
            heading=_("Header Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("region_slider_image"),
                FieldPanel("region_slider_image_alt_text"),
            ],
            heading=_("Region Slider Background Image"),
        ),
        PageChooserPanel("stories_section"),
        MultiFieldPanel(
            [
                ImageChooserPanel("giving_initiative_background_image"),
                FieldPanel("giving_initiative_background_image_alt_text"),
                FieldPanel("giving_initiative_title"),
                FieldPanel("giving_initiative_body"),
            ],
            heading=_("Giving Initiative Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("director_name"),
                ImageChooserPanel("director_image"),
                FieldPanel("director_image_alt_text"),
                FieldPanel("director_phone_number"),
                FieldPanel("region_website_link"),
                FieldPanel("region_facebook_link"),
            ],
            heading=_("Director section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("population_number"),
                FieldPanel("spiritualy_lost"),
                FieldPanel("unreached_people_groups"),
                FieldPanel("ag_constituents"),
                FieldPanel("ag_churches"),
                FieldPanel("ag_ministers"),
                FieldPanel("missionaries_and_associates"),
            ],
            heading=_("Statistics section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("join_the_team_button"),
                FieldPanel("stories_header_title"),
                FieldPanel("stories_header_sub_title"),
                FieldPanel("stories_read_all_button_text"),
                FieldPanel("giving_initiative_header_title"),
                FieldPanel("start_your_gift_button"),
                FieldPanel("director_header_title"),
                FieldPanel("related_ministries_links_text"),
                FieldPanel("phone_number_text"),
                FieldPanel("view_button"),
                FieldPanel("regional_web_site_button"),
                FieldPanel("population_section_title"),
                FieldPanel("spiritually_lost_card_text"),
                FieldPanel("unreached_people_groups_card_text"),
                FieldPanel("ag_constituents_card_text"),
                FieldPanel("ag_churches_card_text"),
                FieldPanel("ag_ministers_card_text"),
                FieldPanel("missionaries_and_associates_card_text"),
            ],
            heading=_("Translatable Specific Regions Page Buttons and Text fields"),
        ),
    ]
    additional_search_fields = [
        index.SearchField("header_sub_text", partial_match=True),
        index.SearchField("header_bottom_text", partial_match=True),
        index.SearchField("giving_initiative_title", partial_match=True),
        index.SearchField("giving_initiative_body", partial_match=True),
        index.SearchField("director_name", partial_match=True),
        index.SearchField("director_image_alt_text", partial_match=True),
        index.SearchField("director_phone_number", partial_match=True),
        index.SearchField("region_website_link", partial_match=True),
        index.SearchField("region_facebook_link", partial_match=True),
        index.SearchField("population_number", partial_match=True),
        index.SearchField("spiritualy_lost", partial_match=True),
        index.SearchField("unreached_people_groups", partial_match=True),
        index.SearchField("ag_constituents", partial_match=True),
        index.SearchField("ag_churches", partial_match=True),
        index.SearchField("ag_ministers", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class RegionIndexPage(Page):
    """Index page for regions"""

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )
    header_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown in the background of the header portion of the region page"
        ),
    )
    header_background_image_alt_text = models.CharField(
        _("Header Background Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the header background image"),
    )
    greg_mundis_section = models.ForeignKey(
        "cms.GregMundisInitiative",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Greg mundis section of the page"),
        verbose_name=_("Greg Mundis Section"),
    )
    mission_text = models.CharField(
        _("Mission Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text in the mission section of the Region Page"),
    )
    africa_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the Africa region"),
    )
    africa_image_alt_text = models.CharField(
        _("Africa Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the Africa region image"),
    )
    asia_pacific_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the Asia Pacific region"),
    )
    asia_pacific_image_alt_text = models.CharField(
        _("Asia Pacific Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the Asia Pacific region image"),
    )
    eurasia_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the Eurasia region"),
    )
    eurasia_image_alt_text = models.CharField(
        _("Eurasia Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the Eurasia region image"),
    )
    europe_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the Europe region"),
    )
    europe_image_alt_text = models.CharField(
        _("Europe Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the Europe region image"),
    )
    international_ministries_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the international ministries"),
    )
    international_ministries_image_alt_text = models.CharField(
        _("International Ministries Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the International Ministries image"),
    )
    latin_america_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the Latin America region"),
    )
    latin_america_image_alt_text = models.CharField(
        _("Latin America Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the Latin America region image"),
    )
    northern_asia_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the Northern America region"),
    )
    northern_asia_image_alt_text = models.CharField(
        _("Northern America Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the Northern America region image"),
    )
    find_more_button = models.CharField(
        _("Find More Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for the Find more button"),
    )
    region_map_header_title = models.CharField(
        _("Region Map Header Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Set text for Region Map Header Title"),
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        ImageChooserPanel("header_background_image"),
        FieldPanel("header_background_image_alt_text"),
        MultiFieldPanel(
            [
                FieldPanel("find_more_button"),
                FieldPanel("region_map_header_title"),
            ],
            heading=_("Translatable Regions Page Buttons and Text fields"),
        ),
        PageChooserPanel("greg_mundis_section"),
        FieldPanel("mission_text"),
        ImageChooserPanel("africa_image"),
        FieldPanel("africa_image_alt_text"),
        ImageChooserPanel("asia_pacific_image"),
        FieldPanel("asia_pacific_image_alt_text"),
        ImageChooserPanel("eurasia_image"),
        FieldPanel("eurasia_image_alt_text"),
        ImageChooserPanel("europe_image"),
        FieldPanel("europe_image_alt_text"),
        ImageChooserPanel("international_ministries_image"),
        FieldPanel("international_ministries_image_alt_text"),
        ImageChooserPanel("latin_america_image"),
        FieldPanel("latin_america_image_alt_text"),
        ImageChooserPanel("northern_asia_image"),
        FieldPanel("northern_asia_image_alt_text"),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["RegionPage"]

    additional_search_fields = [
        index.SearchField("introduction", partial_match=True),
        index.SearchField("mission_text", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    def children(self):
        return self.get_children().specific().live()
