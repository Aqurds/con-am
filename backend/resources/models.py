from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _

from home.utils import get_upload_path


class ResourcesPage(Page):
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
    stories_section = models.ForeignKey(
        "stories.StoryIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Stories section of the page"),
        verbose_name=_("Stories Section"),
    )
    photos_section = models.ForeignKey(
        "photos.PhotoIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Photos section of the page"),
        verbose_name=_("Photos Section"),
    )
    videos_section = models.ForeignKey(
        "videos.VideoIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Videos section of the page"),
        verbose_name=_("Videos Section"),
    )
    world_view_section = models.ForeignKey(
        "world_view.WorldViewIndexPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("World view & more section of the page"),
        verbose_name=_("World View Section"),
    )

    vital_stats_file = models.FileField(
        _("Vital Stats"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_("PDF file for the vital stats"),
    )
    agwm_shop_url = models.CharField(
        _("AGWM Shop URL"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set url to AGWM shop"),
    )
    stories_card_text = models.CharField(
        _("Stories Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Stories Card"),
    )
    photos_card_text = models.CharField(
        _("Photos Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Photos Card"),
    )
    videos_card_text = models.CharField(
        _("Videos Card Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Videos Card"),
    )
    world_view_section_title = models.CharField(
        _("World View Section Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the World View Section Title"),
    )
    world_view_view_all_button = models.CharField(
        _("World View View All Button"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the World View View All Button"),
    )
    world_view_section_sub_title = models.TextField(
        _("World View Section Sub Title"),
        null=True,
        blank=True,
        help_text=_("Set the text for the World View Section Sub Title"),
    )
    vital_stats_header_title = models.CharField(
        _("Vital Stats Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Vital Stats Header Title"),
    )
    vital_stats_sub_title = models.CharField(
        _("Vital Stats Sub Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Vital Stats Sub Title"),
    )
    vital_stats_view_button = models.CharField(
        _("Vital Stats View Button"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Vital Stats View Button"),
    )
    resource_center_header_title = models.CharField(
        _("Resource Center Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Resource Center Header Title"),
    )
    resource_center_go_to_shop_button = models.CharField(
        _("Resource Center Go To Shop Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Go to Shop Button"),
    )
    resource_center_sub_title = models.CharField(
        _("Resource Center Sub Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Set the text for the Resource Center Sub Title"),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        PageChooserPanel("stories_section"),
        PageChooserPanel("photos_section"),
        PageChooserPanel("videos_section"),
        PageChooserPanel("world_view_section"),
        FieldPanel("vital_stats_file"),
        FieldPanel("agwm_shop_url"),
        InlinePanel(
            "featured_resource_products",
            label=_("Featured Resource Products"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("stories_card_text"),
                FieldPanel("photos_card_text"),
                FieldPanel("videos_card_text"),
                FieldPanel("world_view_section_title"),
                FieldPanel("world_view_section_sub_title"),
                FieldPanel("world_view_view_all_button"),
                FieldPanel("vital_stats_header_title"),
                FieldPanel("vital_stats_sub_title"),
                FieldPanel("vital_stats_view_button"),
                FieldPanel("resource_center_header_title"),
                FieldPanel("resource_center_sub_title"),
                FieldPanel("resource_center_go_to_shop_button"),
            ],
            heading="Translatable Resources page buttons and text fields",
        ),
    ]

    additional_search_fields = [
        index.SearchField("agwm_shop_url", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class FeaturedResourceCenterProduct(Orderable):
    page = ParentalKey(
        ResourcesPage,
        on_delete=models.CASCADE,
        null=True,
        related_name="featured_resource_products",
    )
    name = models.CharField(
        _("Name"), max_length=100, help_text=_("Name of the featured product")
    )
    image = models.ImageField(
        _("Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_("Image of the featured product"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the image of the featured resource center product"),
    )
    description = models.CharField(
        _("Price Text"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Description and price of the featured product"),
    )
    footer_text = models.CharField(
        _("Footer Text"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Footer text of the featured product"),
    )
    url = models.CharField(
        _("URL"),
        max_length=150,
        blank=True,
        null=True,
        help_text=_("URL of the store"),
    )
    is_subscription = models.BooleanField(
        _("Is Subscription"),
        default=False,
        help_text=_(
            "Determines whether the product is a subscription-based product or not"
        ),
    )
    subscription_link = models.CharField(
        _("Subscription URL"),
        max_length=150,
        blank=True,
        null=True,
        help_text=_("Link to the subscription-based product"),
    )

    def __str__(self):
        return self.name
