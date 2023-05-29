from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ExploreWaysToServe(Page):
    """Page for the Explore Ways to Serve"""

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
    header_tab_short_term_text = models.CharField(
        _("Short Term Tab Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Short term tab text in header."),
    )
    header_tab_one_to_two_year_text = models.CharField(
        _("1 - 2 Year Tab Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("1 - 2 year term tab text in header."),
    )
    header_tab_career_text = models.CharField(
        _("Career Tab Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Career tab text in header."),
    )
    # Short Term Tab/Section
    short_term_header_title = models.CharField(
        _("Short Term Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text that will be shown in the header portion for when the user clicks the Short Term tab"
        ),
    )
    short_term_section_title = models.CharField(
        _("Short Term Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown below the 3 inner tabs of the short term section"
        ),
    )
    short_term_first_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "First out of three images that will be shown in the page which are above the qualifications section."
        ),
    )
    short_term_first_image_alt_text = models.CharField(
        _("Short Term First Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Short Term First Image"),
    )
    short_term_first_image_text = models.CharField(
        _("Short Term First Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown on the first image in the short term section. Example 'Reach the Unreached'"
        ),
    )
    short_term_second_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Second out of three images that will be shown in the page which are above the qualifications section"
        ),
    )
    short_term_second_image_alt_text = models.CharField(
        _("Short Term Second Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Short Term Second Image"),
    )
    short_term_second_image_text = models.CharField(
        _("Short Term Second Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown on the second image in the short term section. Example 'Refine Your Skills'"
        ),
    )
    short_term_third_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Third out of three images that will be shown in the page which are above the qualifications section"
        ),
    )
    short_term_third_image_alt_text = models.CharField(
        _("Short Term Third Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Short Term Third Image"),
    )
    short_term_third_image_text = models.CharField(
        _("Short Term Third Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown on the third image in the short term section. Example 'Gain Real Experience'"
        ),
    )

    # Short term first tab contents
    short_term_first_tab_title = models.CharField(
        _("Short Term First Tab Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the first tab of the short term trips"),
    )
    short_term_first_tab_bottom_text = models.CharField(
        _("Short Term First Tab Bottom Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the first tab title"),
    )
    short_term_first_tab_first_section_title = models.CharField(
        _("Short Term First Tab First Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text that will be shown at the start of the page. Example 'Short-Term (Under 31 days)'"
        ),
    )
    short_term_first_tab_first_section_content = models.TextField(
        _("Short Term First Tab First Section Content"),
        null=True,
        blank=True,
        help_text=_(
            "Content text will be shown under the first section title of the page"
        ),
    )
    short_term_first_tab_qualifications_section_title = models.CharField(
        _("Short Term First Tab Qualifications Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the qualifications section of the page"),
    )
    short_term_first_tab_qualifications_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown for the qualifications section of the page."
        ),
    )
    short_term_first_tab_qualifications_image_alt_text = models.CharField(
        _("Short Term First Tab Qualifications Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the qualifications image"),
    )
    short_term_opportunity_section_title = models.CharField(
        _("Short Term Opportunity Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown as the title in the Opportunities section of the page"
        ),
    )
    first_opportunity_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the first opportunity."),
    )
    first_opportunity_image_alt_text = models.CharField(
        _("First Opportunity Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the First Opportunity Image"),
    )
    first_opportunity_title = models.CharField(
        _("First Opportunity Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title of the first opportunity"),
    )
    first_opportunity_button_url = models.TextField(
        _("First Opportunity Button URL"),
        null=True,
        blank=True,
        help_text=_(
            "URL for the first button of the opportunities section of the page"
        ),
    )
    first_opportunity_content = models.TextField(
        _("First Opportunity Content"),
        null=True,
        blank=True,
        help_text=_("Content for the first opportunity"),
    )
    second_opportunity_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown for the second opportunity."),
    )
    second_opportunity_image_alt_text = models.CharField(
        _("Second Opportunity Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Second Opportunity Image"),
    )
    second_opportunity_title = models.CharField(
        _("Second Opportunity Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title of the second opportunity"),
    )
    second_opportunity_content = RichTextField(
        _("Second Opportunity Content"),
        null=True,
        blank=True,
        help_text=_("Content for the second opportunity"),
    )
    second_opportunity_button_url = models.TextField(
        _("Second Opportunity Button URL"),
        null=True,
        blank=True,
        help_text=_(
            "URL for the second button of the opportunities section of the page"
        ),
    )
    begin_application_button_text = models.CharField(
        _("Begin Application Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Begin application button text at the bottom of the opportunity section."),
    )
    email_mapstreams_button_text = models.CharField(
        _("Email Mapstreams Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Email mapstreams button text at the bottom of the opportunity section."),
    )
    last_section_title = models.CharField(
        _("Last Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title for the last section of the page. Example 'Invited Guests'"),
    )
    last_section_first_content = RichTextField(
        _("Last Section First Content"),
        null=True,
        blank=True,
        help_text=_("Content under the last section title"),
    )
    last_section_button_url = models.TextField(
        _("Last Section Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the button on the last section of the page"),
    )
    last_section_second_content = RichTextField(
        _("Last Section Second Content"),
        null=True,
        blank=True,
        help_text=_("Content under the button of the last section of the page"),
    )
    last_section_button_text = models.CharField(
        _("Last Section Button Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Button text at the last section of the page."),
    )

    # Short term second tab contents
    short_term_second_tab_title = models.CharField(
        _("Short Term Second Tab Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the second tab of the short term trips"),
    )
    short_term_second_tab_bottom_text = models.CharField(
        _("Short Term Second Tab Bottom Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the second tab title"),
    )
    short_term_second_tab_first_section_title = models.CharField(
        _("Short Term Second Tab First Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text that will be shown at the start of the page. Example 'Ministers Abroad'"
        ),
    )
    short_term_second_tab_first_section_content = RichTextField(
        _("Short Term Second Tab First section Content"),
        null=True,
        blank=True,
        help_text=_("Content text will be shown under the title of the page"),
    )
    short_term_second_tab_qualifications_section_title = models.CharField(
        _("Short Term Second Tab Qualifications Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the qualifications section of the page"),
    )
    short_term_second_tab_qualifications_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown for the qualifications section of the page."
        ),
    )
    short_term_second_tab_qualifications_image_alt_text = models.CharField(
        _("Short Term Second Tab Qualifications Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the qualifications image"),
    )
    short_term_second_tab_last_section_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background image that will be shown for the bottom section of the page."
        ),
    )
    short_term_second_tab_last_section_background_image_alt_text = models.CharField(
        _("Short Term Second Tab Last Section Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Last Section Background Image"),
    )
    short_term_second_tab_last_section_title = models.CharField(
        _("Short Term Second Tab Last Section Title"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Title text that will be shown in the last section of the page"),
    )
    short_term_second_tab_last_section_content = RichTextField(
        _("Short Term Second Tab Last Section Content"),
        null=True,
        blank=True,
        help_text=_("Content text for the last section of the page"),
    )
    short_term_second_tab_email = models.EmailField(
        _("Short Term Second Tab Email"),
        null=True,
        blank=True,
        help_text=_(
            "Email Address for the second tab of the page. This will be used as the email address for the button in the bottom section of the page"
        ),
    )

    # Short term third tab contents
    short_term_third_tab_title = models.CharField(
        _("Short Term Third Tab Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the third tab of the short term trips"),
    )
    short_term_third_tab_bottom_text = models.CharField(
        _("Short Term Third Tab Bottom Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the third tab title"),
    )
    short_term_third_tab_first_section_title = models.CharField(
        _("Short Term Third Tab First Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text that will be shown at the start of the page. Example 'Missions Abroad Placement Services (MAPS)'"
        ),
    )
    short_term_third_tab_first_section_content = models.TextField(
        _("Short Term Second Tab First Section Content"),
        null=True,
        blank=True,
        help_text=_("Content text will be shown under the title of the page"),
    )
    short_term_third_tab_qualifications_section_title = models.CharField(
        _("Short Term Third Tab Qualifications Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the qualifications section of the page"),
    )
    short_term_third_tab_qualifications_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown for the qualifications section of the page."
        ),
    )
    short_term_third_tab_qualifications_image_alt_text = models.CharField(
        _("Short Term Third Tab Qualifications Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the qualifications image"),
    )
    short_term_third_tab_last_section_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background image that will be shown for the bottom section of the page."
        ),
    )
    short_term_third_tab_last_section_background_image_alt_text = models.CharField(
        _("Short Term Third Tab Last Section Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Last Section Background Image"),
    )
    short_term_third_tab_last_section_title = models.CharField(
        _("Short Term Third Tab Last Section Title"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Title text that will be shown in the last section of the page"),
    )
    short_term_third_tab_last_section_content = models.TextField(
        _("Short Term Third Tab Last Section Content"),
        null=True,
        blank=True,
        help_text=_("Content text for the last section of the page"),
    )
    short_term_third_tab_first_button_url = models.TextField(
        _("Short Term Third Tab First Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the first button"),
    )
    short_term_third_tab_second_button_url = models.TextField(
        _("Short Term Third Tab Second Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the second button"),
    )
    short_term_third_tab_third_button_url = models.TextField(
        _("Short Term Third Tab Third Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the third button"),
    )

    # 1-2 Year Section
    one_to_two_year_header_title = models.CharField(
        _("One To Two Year Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text that will be shown in the header portion for when the user clicks the One to Two Year tab"
        ),
    )
    one_to_two_year_header_content = models.TextField(
        _("One To Two Year Header Content"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the header title"),
    )
    one_to_two_year_first_section_title = models.TextField(
        _("One To Two Year First Section Title"),
        null=True,
        blank=True,
        help_text=_(
            "Title of the first section of the page. Example 'Don't miss this moment etc..'"
        ),
    )
    one_to_two_year_first_section_content = RichTextField(
        _("One To Two Year First Section Content"),
        null=True,
        blank=True,
        help_text=_("Content under the first section title"),
    )
    one_to_two_year_video_thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Thumbnail for the video in the 1-2 Year page"),
    )
    one_to_two_year_video_thumbnail_alt_text = models.CharField(
        _("One To Two Year Video Thumbnail Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the video thumbnail of the 1-2 year page"),
    )
    one_to_two_year_video_url = models.TextField(
        _("One To Two Year Video URL"),
        null=True,
        blank=True,
        help_text=_(
            "URL for the featured video of the page. This needs to be the embed URL of the video or else the video player will not work"
        ),
    )
    one_to_two_year_start_today_button_text = models.CharField(
        _("One To Two Year Start Today Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text for the start today button of the page"),
    )
    one_to_two_year_start_today_button_url = models.TextField(
        _("One To Two Year Start Today Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the start today button of the page"),
    )
    one_to_two_year_second_section_title = models.CharField(
        _("One To Two Year Second Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text for the second section of the page. Example 'Missionary Associate'"
        ),
    )
    one_to_two_year_second_section_content = RichTextField(
        _("One To Two Year Second Section Content"),
        null=True,
        blank=True,
        help_text=_("Content for the second section"),
    )
    one_to_two_year_image_section_first_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "First image that will be shown for the image section of the page."
        ),
    )
    one_to_two_year_image_section_first_image_alt_text = models.CharField(
        _("One To Two Year Image Section First Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the first image in the image section"),
    )
    one_to_two_year_image_section_first_image_text = models.CharField(
        _("One To Two Year Image Section First Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown in the first image of the image section"),
    )
    one_to_two_year_image_section_second_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Second image that will be shown for the image section of the page."
        ),
    )
    one_to_two_year_image_section_second_image_alt_text = models.CharField(
        _("One To Two Year Image Section Second Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the second image in the image section"),
    )
    one_to_two_year_image_section_second_image_text = models.CharField(
        _("One To Two Year Image Section Second Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown in the second image of the image section"),
    )
    one_to_two_year_image_section_third_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Second image that will be shown for the image section of the page."
        ),
    )
    one_to_two_year_image_section_third_image_alt_text = models.CharField(
        _("One To Two Year Image Section Third Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the third image in the image section"),
    )
    one_to_two_year_image_section_third_image_text = models.CharField(
        _("One To Two Year Image Section Third Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown in the third image of the image section"),
    )
    one_to_two_year_application_section_title = models.CharField(
        _("One To Two Year Application Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text for the application section of the page. Example 'The Application Process'"
        ),
    )
    one_to_two_year_apply_now_button_text = models.CharField(
        _("One To Two Year Apply Now Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text for the 'Apply Now' button"),
    )
    one_to_two_year_apply_now_button_url = models.TextField(
        _("One To Two Year Apply Now Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the 'Apply Now' button"),
    )
    one_to_two_year_qualifications_section_title = models.CharField(
        _("One To Two Year Qualifications Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the qualifications section of the page"),
    )
    one_to_two_year_qualifications_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown for the qualifications section of the page."
        ),
    )
    one_to_two_year_qualifications_image_alt_text = models.CharField(
        _("One To Two Year Qualifications Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the qualifications image"),
    )
    one_to_two_year_qualifications_button_text = models.CharField(
        _("One To Two Year Qualifications Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text for the qualifications button"),
    )
    one_to_two_year_qualifications_button_url = models.TextField(
        _("One To Two Year Qualifications Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the qualifications button"),
    )
    one_to_two_year_last_section_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background image that will be shown for the bottom section of the page."
        ),
    )
    one_to_two_year_last_section_background_image_alt_text = models.CharField(
        _("One To Two Year Last Section Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Last Section Background Image"),
    )
    one_to_two_year_last_section_title = models.CharField(
        _("One To Two Year Last Section Title"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Title text that will be shown in the last section of the page"),
    )
    one_to_two_year_last_section_content = models.TextField(
        _("One To Two Year Last Section Content"),
        null=True,
        blank=True,
        help_text=_("Content text for the last section of the page"),
    )
    one_to_two_year_last_section_first_button_url = models.TextField(
        _("One To Two Year Last Section First Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the first button"),
    )
    one_to_two_year_last_section_second_button_url = models.TextField(
        _("One To Two Year Last Section Second Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the second button"),
    )
    one_to_two_year_last_section_third_button_url = models.TextField(
        _("One To Two Year Last Section Third Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the third button"),
    )
    one_to_two_year_last_section_first_button_text = models.CharField(
        _("One To Two Year Last Section First Button Text"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Text for the first button"),
    )
    one_to_two_year_last_section_second_button_text = models.CharField(
        _("One To Two Year Last Section Second Button Text"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Text for the second button"),
    )
    one_to_two_year_last_section_third_button_text = models.CharField(
        _("One To Two Year Last Section Third Button Text"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Text for the third button"),
    )

    # Career section
    career_header_title = models.CharField(
        _("Career Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text that will be shown in the header portion for when the user clicks the Career tab"
        ),
    )
    career_header_content = models.TextField(
        _("Career Header Content"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the header title"),
    )
    career_first_section_title = models.TextField(
        _("Career First Section Title"),
        null=True,
        blank=True,
        help_text=_(
            "Title of the first section of the page. Example 'Create generational transformation'"
        ),
    )
    career_first_section_content = RichTextField(
        _("Career First Section Content"),
        null=True,
        blank=True,
        help_text=_("Content under the first section title"),
    )
    career_video_thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Thumbnail for the video in the Career page"),
    )
    career_video_thumbnail_alt_text = models.CharField(
        _("Career Video Thumbnail Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the video thumbnail of the Career page"),
    )
    career_video_url = models.TextField(
        _("Career Video URL"),
        null=True,
        blank=True,
        help_text=_(
            "URL for the featured video of the page. This needs to be the embed URL of the video or else the video player will not work"
        ),
    )
    career_start_today_button_url = models.TextField(
        _("Career Start Today Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the start today button of the page"),
    )
    career_second_section_title = models.CharField(
        _("Career Second Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text for the second section of the page. Example 'Career Missionary'"
        ),
    )
    career_second_section_content = RichTextField(
        _("Career Second Section Content"),
        null=True,
        blank=True,
        help_text=_("Content for the second section"),
    )
    career_image_section_first_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "First image that will be shown for the image section of the page."
        ),
    )
    career_image_section_first_image_alt_text = models.CharField(
        _("Career Image Section First Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the first image in the image section"),
    )
    career_image_section_first_image_text = models.CharField(
        _("Career Image Section First Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown in the first image of the image section"),
    )
    career_image_section_second_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Second image that will be shown for the image section of the page."
        ),
    )
    career_image_section_second_image_alt_text = models.CharField(
        _("Career Image Section Second Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the second image in the image section"),
    )
    career_image_section_second_image_text = models.CharField(
        _("Career Image Section Second Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown in the second image of the image section"),
    )
    career_image_section_third_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Second image that will be shown for the image section of the page."
        ),
    )
    career_image_section_third_image_alt_text = models.CharField(
        _("Career Image Section Third Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the third image in the image section"),
    )
    career_image_section_third_image_text = models.CharField(
        _("Career Image Section Third Image Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text that will be shown in the third image of the image section"),
    )
    career_application_section_title = models.CharField(
        _("Career Application Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Title text for the application section of the page. Example 'The Application Process'"
        ),
    )
    career_apply_now_button_text = models.CharField(
        _("Career Apply Now Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text for the 'Apply Now' button"),
    )
    career_apply_now_button_url = models.TextField(
        _("Career Apply Now Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the 'Apply Now' button"),
    )
    career_qualifications_section_title = models.CharField(
        _("Career Qualifications Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the qualifications section of the page"),
    )
    career_qualifications_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that will be shown for the qualifications section of the page."
        ),
    )
    career_qualifications_image_alt_text = models.CharField(
        _("Career Qualifications Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the qualifications image"),
    )
    career_qualifications_button_text = models.CharField(
        _("Career Qualifications Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text for the qualifications button"),
    )
    career_qualifications_button_url = models.TextField(
        _("Career Qualifications Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the qualifications button"),
    )
    career_last_section_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Background image that will be shown for the bottom section of the page."
        ),
    )
    career_last_section_background_image_alt_text = models.CharField(
        _("Career Last Section Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the Last Section Background Image"),
    )
    career_last_section_title = models.CharField(
        _("Career Last Section Title"),
        max_length=255,
        null=255,
        blank=255,
        help_text=_("Title text that will be shown in the last section of the page"),
    )
    career_last_section_content = models.TextField(
        _("Career Last Section Content"),
        null=True,
        blank=True,
        help_text=_("Content text for the last section of the page"),
    )
    career_last_section_button_text = models.TextField(
        _("Career Last Section Button Text"),
        null=True,
        blank=True,
        help_text=_("Text for the Last Section button"),
    )
    career_last_section_button_url = models.TextField(
        _("Career Last Section Button URL"),
        null=True,
        blank=True,
        help_text=_("URL for the Last Section button"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        MultiFieldPanel(
            [
                FieldPanel("header_tab_short_term_text"),
                FieldPanel("header_tab_one_to_two_year_text"),
                FieldPanel("header_tab_career_text"),
            ],
            heading="Tab Buttons Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("short_term_header_title"),
                FieldPanel("short_term_section_title"),
                ImageChooserPanel("short_term_first_image"),
                FieldPanel("short_term_first_image_alt_text"),
                FieldPanel("short_term_first_image_text"),
                ImageChooserPanel("short_term_second_image"),
                FieldPanel("short_term_second_image_alt_text"),
                FieldPanel("short_term_second_image_text"),
                ImageChooserPanel("short_term_third_image"),
                FieldPanel("short_term_third_image_alt_text"),
                FieldPanel("short_term_third_image_text"),
                FieldPanel("short_term_first_tab_title"),
                FieldPanel("short_term_first_tab_bottom_text"),
                FieldPanel("short_term_first_tab_first_section_title"),
                FieldPanel("short_term_first_tab_first_section_content"),
                FieldPanel("short_term_first_tab_qualifications_section_title"),
                ImageChooserPanel("short_term_first_tab_qualifications_image"),
                FieldPanel("short_term_first_tab_qualifications_image_alt_text"),
                FieldPanel("short_term_opportunity_section_title"),
                ImageChooserPanel("first_opportunity_image"),
                FieldPanel("first_opportunity_image_alt_text"),
                FieldPanel("first_opportunity_title"),
                FieldPanel("first_opportunity_button_url"),
                FieldPanel("first_opportunity_content"),
                InlinePanel(
                    "short_term_first_tab_qualification",
                    label=_("Short Term First Tab Qualification"),
                ),
                ImageChooserPanel("second_opportunity_image"),
                FieldPanel("second_opportunity_image_alt_text"),
                FieldPanel("second_opportunity_title"),
                FieldPanel("second_opportunity_content"),
                FieldPanel("second_opportunity_button_url"),
                FieldPanel("begin_application_button_text"),
                FieldPanel("email_mapstreams_button_text"),
                FieldPanel("last_section_title"),
                FieldPanel("last_section_first_content"),
                FieldPanel("last_section_button_url"),
                FieldPanel("last_section_second_content"),
                FieldPanel("last_section_button_text"),
                FieldPanel("short_term_second_tab_title"),
                FieldPanel("short_term_second_tab_bottom_text"),
                FieldPanel("short_term_second_tab_first_section_title"),
                FieldPanel("short_term_second_tab_first_section_content"),
                FieldPanel("short_term_second_tab_qualifications_section_title"),
                ImageChooserPanel("short_term_second_tab_qualifications_image"),
                FieldPanel("short_term_second_tab_qualifications_image_alt_text"),
                InlinePanel(
                    "short_term_second_tab_qualification",
                    label=_("Short Term Second Tab Qualification"),
                ),
                ImageChooserPanel(
                    "short_term_second_tab_last_section_background_image"
                ),
                FieldPanel(
                    "short_term_second_tab_last_section_background_image_alt_text"
                ),
                FieldPanel("short_term_second_tab_last_section_title"),
                FieldPanel("short_term_second_tab_last_section_content"),
                FieldPanel("short_term_second_tab_email"),
                FieldPanel("short_term_third_tab_title"),
                FieldPanel("short_term_third_tab_bottom_text"),
                FieldPanel("short_term_third_tab_first_section_title"),
                FieldPanel("short_term_third_tab_first_section_content"),
                FieldPanel("short_term_third_tab_qualifications_section_title"),
                ImageChooserPanel("short_term_third_tab_qualifications_image"),
                FieldPanel("short_term_third_tab_qualifications_image_alt_text"),
                InlinePanel(
                    "short_term_third_tab_qualification",
                    label=_("Short Term Third Tab Qualification"),
                ),
                ImageChooserPanel("short_term_third_tab_last_section_background_image"),
                FieldPanel(
                    "short_term_third_tab_last_section_background_image_alt_text"
                ),
                FieldPanel("short_term_third_tab_last_section_title"),
                FieldPanel("short_term_third_tab_last_section_content"),
                FieldPanel("short_term_third_tab_first_button_url"),
                FieldPanel("short_term_third_tab_second_button_url"),
                FieldPanel("short_term_third_tab_third_button_url"),
            ],
            heading="Short-term Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("one_to_two_year_header_title"),
                FieldPanel("one_to_two_year_header_content"),
                FieldPanel("one_to_two_year_first_section_title"),
                FieldPanel("one_to_two_year_first_section_content"),
                InlinePanel(
                    "one_to_two_year_gallery",
                    label="Image/Video for Image/Video Slider",
                ),
                FieldPanel("one_to_two_year_start_today_button_text"),
                FieldPanel("one_to_two_year_start_today_button_url"),
                FieldPanel("one_to_two_year_second_section_title"),
                FieldPanel("one_to_two_year_second_section_content"),
                ImageChooserPanel("one_to_two_year_image_section_first_image"),
                FieldPanel("one_to_two_year_image_section_first_image_alt_text"),
                FieldPanel("one_to_two_year_image_section_first_image_text"),
                ImageChooserPanel("one_to_two_year_image_section_second_image"),
                FieldPanel("one_to_two_year_image_section_second_image_alt_text"),
                FieldPanel("one_to_two_year_image_section_second_image_text"),
                ImageChooserPanel("one_to_two_year_image_section_third_image"),
                FieldPanel("one_to_two_year_image_section_third_image_alt_text"),
                FieldPanel("one_to_two_year_image_section_third_image_text"),
                FieldPanel("one_to_two_year_application_section_title"),
                FieldPanel("one_to_two_year_apply_now_button_text"),
                FieldPanel("one_to_two_year_apply_now_button_url"),
                InlinePanel(
                    "one_to_two_year_application_process",
                    label=_("1-2 Year Application Process"),
                ),
                FieldPanel("one_to_two_year_qualifications_section_title"),
                ImageChooserPanel("one_to_two_year_qualifications_image"),
                FieldPanel("one_to_two_year_qualifications_image_alt_text"),
                FieldPanel("one_to_two_year_qualifications_button_text"),
                FieldPanel("one_to_two_year_qualifications_button_url"),
                InlinePanel(
                    "one_to_two_year_qualification",
                    label=_("1-2 Year Qualification"),
                ),
                ImageChooserPanel("one_to_two_year_last_section_background_image"),
                FieldPanel("one_to_two_year_last_section_background_image_alt_text"),
                FieldPanel("one_to_two_year_last_section_title"),
                FieldPanel("one_to_two_year_last_section_content"),
                FieldPanel("one_to_two_year_last_section_first_button_text"),
                FieldPanel("one_to_two_year_last_section_first_button_url"),
                FieldPanel("one_to_two_year_last_section_second_button_text"),                
                FieldPanel("one_to_two_year_last_section_second_button_url"),
                FieldPanel("one_to_two_year_last_section_third_button_text"),
                FieldPanel("one_to_two_year_last_section_third_button_url"),
            ],
            heading="1-2 Year Section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("career_header_title"),
                FieldPanel("career_header_content"),
                FieldPanel("career_first_section_title"),
                FieldPanel("career_first_section_content"),
                InlinePanel(
                    "career_gallery", label="Image/Video for Image/Video Slider"
                ),
                FieldPanel("career_start_today_button_url"),
                FieldPanel("career_second_section_title"),
                FieldPanel("career_second_section_content"),
                ImageChooserPanel("career_image_section_first_image"),
                FieldPanel("career_image_section_first_image_alt_text"),
                FieldPanel("career_image_section_first_image_text"),
                ImageChooserPanel("career_image_section_second_image"),
                FieldPanel("career_image_section_second_image_alt_text"),
                FieldPanel("career_image_section_second_image_text"),
                ImageChooserPanel("career_image_section_third_image"),
                FieldPanel("career_image_section_third_image_alt_text"),
                FieldPanel("career_image_section_third_image_text"),
                FieldPanel("career_application_section_title"),
                FieldPanel("career_apply_now_button_text"),
                FieldPanel("career_apply_now_button_url"),
                InlinePanel(
                    "career_application_process",
                    label=_("Career Application Process"),
                ),
                FieldPanel("career_qualifications_section_title"),
                ImageChooserPanel("career_qualifications_image"),
                FieldPanel("career_qualifications_image_alt_text"),
                FieldPanel("career_qualifications_button_text"),
                FieldPanel("career_qualifications_button_url"),
                InlinePanel("career_qualification", label=_("Career Qualification")),
                ImageChooserPanel("career_last_section_background_image"),
                FieldPanel("career_last_section_background_image_alt_text"),
                FieldPanel("career_last_section_title"),
                FieldPanel("career_last_section_content"),
                FieldPanel("career_last_section_button_text"),
                FieldPanel("career_last_section_button_url"),
            ],
            heading="Career Section",
        ),
    ]
    additional_search_fields = [
        index.SearchField("short_term_header_title", partial_match=True),
        index.SearchField("short_term_section_title", partial_match=True),
        index.SearchField("short_term_first_tab_title", partial_match=True),
        index.SearchField("short_term_first_tab_bottom_text", partial_match=True),
        index.SearchField("short_term_first_tab_bottom_text", partial_match=True),
        index.SearchField(
            "short_term_first_tab_first_section_title", partial_match=True
        ),
        index.SearchField(
            "short_term_first_tab_first_section_content", partial_match=True
        ),
        index.SearchField(
            "short_term_first_tab_qualifications_section_title", partial_match=True
        ),
        index.SearchField("short_term_opportunity_section_title", partial_match=True),
        index.SearchField("first_opportunity_title", partial_match=True),
        index.SearchField("second_opportunity_title", partial_match=True),
        index.SearchField("second_opportunity_content", partial_match=True),
        index.SearchField("last_section_title", partial_match=True),
        index.SearchField("last_section_first_content", partial_match=True),
        index.SearchField("last_section_second_content", partial_match=True),
        index.SearchField("short_term_second_tab_title", partial_match=True),
        index.SearchField("short_term_second_tab_bottom_text", partial_match=True),
        index.SearchField(
            "short_term_second_tab_first_section_title", partial_match=True
        ),
        index.SearchField(
            "short_term_second_tab_first_section_content", partial_match=True
        ),
        index.SearchField(
            "short_term_second_tab_qualifications_section_title",
            partial_match=True,
        ),
        index.SearchField(
            "short_term_second_tab_last_section_title", partial_match=True
        ),
        index.SearchField(
            "short_term_second_tab_last_section_content", partial_match=True
        ),
        index.SearchField("short_term_second_tab_email", partial_match=True),
        index.SearchField("short_term_third_tab_email", partial_match=True),
        index.SearchField("short_term_third_tab_title", partial_match=True),
        index.SearchField("short_term_third_tab_bottom_text", partial_match=True),
        index.SearchField(
            "short_term_third_tab_first_section_title", partial_match=True
        ),
        index.SearchField(
            "short_term_third_tab_first_section_content", partial_match=True
        ),
        index.SearchField(
            "short_term_third_tab_qualifications_section_title",
            partial_match=True,
        ),
        index.SearchField(
            "short_term_third_tab_last_section_title", partial_match=True
        ),
        index.SearchField(
            "short_term_third_tab_last_section_content", partial_match=True
        ),
        index.SearchField("one_to_two_year_header_title", partial_match=True),
        index.SearchField("one_to_two_year_header_content", partial_match=True),
        index.SearchField("one_to_two_year_header_section_title", partial_match=True),
        index.SearchField("one_to_two_year_header_section_content", partial_match=True),
        index.SearchField("one_to_two_year_second_section_title", partial_match=True),
        index.SearchField("one_to_two_year_second_section_content", partial_match=True),
        index.SearchField(
            "one_to_two_year_application_section_title", partial_match=True
        ),
        index.SearchField(
            "one_to_two_year_qualifications_section_title", partial_match=True
        ),
        index.SearchField("one_to_two_year_last_section_title", partial_match=True),
        index.SearchField("one_to_two_year_last_section_content", partial_match=True),
        index.SearchField("career_header_title", partial_match=True),
        index.SearchField("career_header_content", partial_match=True),
        index.SearchField("career_first_section_title", partial_match=True),
        index.SearchField("career_first_section_content", partial_match=True),
        index.SearchField("career_second_section_title", partial_match=True),
        index.SearchField("career_second_section_content", partial_match=True),
        index.SearchField("career_application_section_title", partial_match=True),
        index.SearchField("career_qualifications_section_title", partial_match=True),
        index.SearchField("career_last_section_title", partial_match=True),
        index.SearchField("career_last_section_content", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class OneToTwoYearSectionGallery(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        related_name="one_to_two_year_gallery",
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
            "Image as part of the gallery. This also serves as the thumbnail if the item of the gallery is a video"
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


class CareerSectionGallery(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        related_name="career_gallery",
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
            "Image as part of the gallery. This also serves as the thumbnail if the item of the gallery is a video"
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


class ShortTermFirstTabQualification(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="short_term_first_tab_qualification",
    )
    qualification = models.TextField(
        _("Qualification"),
        null=True,
        help_text=(_("Text for the qualification of the section")),
    )

    panels = [
        FieldPanel("qualification"),
    ]


class ShortTermSecondTabQualification(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="short_term_second_tab_qualification",
    )
    qualification = models.TextField(
        _("Qualification"),
        null=True,
        help_text=(_("Text for the qualification of the section")),
    )

    panels = [
        FieldPanel("qualification"),
    ]


class ShortTermThirdTabQualification(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="short_term_third_tab_qualification",
    )
    qualification = models.TextField(
        _("Qualification"),
        null=True,
        help_text=(_("Text for the qualification of the section")),
    )

    panels = [
        FieldPanel("qualification"),
    ]


class OneToTwoYearQualification(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="one_to_two_year_qualification",
    )
    qualification = models.TextField(
        _("Qualification"),
        null=True,
        help_text=(_("Text for the qualification of the section")),
    )

    panels = [
        FieldPanel("qualification"),
    ]


class CareerQualification(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="career_qualification",
    )
    qualification = models.TextField(
        _("Qualification"),
        null=True,
        help_text=(_("Text for the qualification of the section")),
    )

    panels = [
        FieldPanel("qualification"),
    ]


class OneToTwoYearApplicationProcess(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="one_to_two_year_application_process",
    )
    title = models.TextField(
        _("Title"), null=True, help_text=_("Title of the application process")
    )
    description = models.TextField(
        _("Description"),
        null=True,
        help_text=_("Description of the application process"),
    )

    panels = [FieldPanel("title"), FieldPanel("description")]


class CareerApplicationProcess(Orderable):
    page = ParentalKey(
        ExploreWaysToServe,
        on_delete=models.CASCADE,
        null=True,
        related_name="career_application_process",
    )
    title = models.TextField(
        _("Title"), null=True, help_text=_("Title of the application process")
    )
    description = models.TextField(
        _("Description"),
        null=True,
        help_text=_("Description of the application process"),
    )

    panels = [FieldPanel("title"), FieldPanel("description")]
