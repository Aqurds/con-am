from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _

from home.utils import get_upload_path


class PrayerPage(Page):
    """Page for prayer"""

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
    pray_header_title = models.CharField(
        _("Prayer Header Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Title for the header title portion of the prayer page."),
    )
    pray_header_body = models.TextField(
        _("Prayer Header Description"),
        null=True,
        blank=True,
        help_text=_("Body for the header description portion of the prayer page."),
    )
    pray_band_title = models.CharField(
        _("Pray Band Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text in the title of the pray band portion of the prayer page."),
    )
    pray_band_body = RichTextField(
        _("Pray Band Body"),
        null=True,
        blank=True,
        help_text=_("Text in the body of the pray band portion of the prayer page."),
    )
    prayer_modal_header_title = models.CharField(
        _("Prayer Modal Header Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Prayer Modal Header Title"),
    )
    social_prayer_feed_section_title = models.CharField(
        _("Social Prayer Feed Section Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer Feed Section Title"),
    )
    social_prayer_feed_section_description = models.CharField(
        _("Social Prayer Feed Section Description"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer Feed Section Description"),
    )
    social_prayer_feed_card_title = models.CharField(
        _("Social Prayer Feed Card Title"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer feed card title"),
    )
    social_prayer_feed_card_description = models.TextField(
        _("Social Prayer Feed Section Description"),
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer feed card description"),
    )
    social_prayer_feed_modal_title = models.CharField(
        _("Social Prayer Feed Modal Title"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer feed modal title"),
    )
    social_prayer_feed_modal_sub_title = models.CharField(
        _("Social Prayer Feed Modal Sub Title"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer feed modal sub title"),
    )
    social_prayer_feed_modal_header_description = models.CharField(
        _("Social Prayer Feed Modal Header Description"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer feed modal header description"),
    )
    social_prayer_feed_modal_body = models.TextField(
        _("Social Prayer Feed Modal Body"),
        null=True,
        blank=True,
        help_text=_("Text of the Social Prayer feed Modal Body"),
    )
    last_section_header_title = models.CharField(
        _("Last Section Header Title"),
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Text of the Last Section Header Title"),
    )
    last_section_facebook_button = models.CharField(
        _("Last Section Facebook Button"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Last Section Facebook Button"),
    )
    last_section_instagram_button = models.CharField(
        _("Last Section Instagram Button"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Last Section Instagram Button"),
    )
    last_section_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_(
            "Image that is going to be displayed in the bottom section of the page."
        ),
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("pray_header_title"),
        FieldPanel("pray_header_body"),
        FieldPanel("pray_band_title"),
        FieldPanel("pray_band_body"),
        ImageChooserPanel("last_section_image"),
        MultiFieldPanel(
            [
                FieldPanel("prayer_modal_header_title"),
                FieldPanel("social_prayer_feed_section_title"),
                FieldPanel("social_prayer_feed_section_description"),
                FieldPanel("social_prayer_feed_card_title"),
                FieldPanel("social_prayer_feed_card_description"),
                FieldPanel("social_prayer_feed_modal_title"),
                FieldPanel("social_prayer_feed_modal_sub_title"),
                FieldPanel("social_prayer_feed_modal_header_description"),
                FieldPanel("social_prayer_feed_modal_body"),
                FieldPanel("last_section_header_title"),
                FieldPanel("last_section_facebook_button"),
                FieldPanel("last_section_instagram_button"),
            ],
            heading="Translatable Prayer page buttons and text",
        ),
    ]

    additional_search_fields = [
        index.SearchField("pray_header_title", partial_match=True),
        index.SearchField("pray_header_body", partial_match=True),
        index.SearchField("pray_band_title", partial_match=True),
        index.SearchField("pray_band_body", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    class Meta:
        verbose_name = _("Prayer Page")
        verbose_name_plural = _("Prayer Pages")


class Prayer(models.Model):
    name = models.CharField(
        _("Prayer Name"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Name of the prayer"),
    )
    name_es = models.CharField(
        _("Prayer Name in Spanish"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Name of the prayer"),
    )
    is_featured_prayer = models.BooleanField(
        _("Is Featured Prayer"),
        default=False,
        null=True,
        help_text=_("Set this to Yes if prayer is to be featured"),
    )
    body = models.TextField(
        _("Body of the Prayer"),
        null=True,
        blank=True,
        help_text=_("Body of the prayer"),
    )
    body_es = models.TextField(
        _("Body of the Prayer in Spanish"),
        null=True,
        blank=True,
        help_text=_("Body of the prayer"),
    )
    image = models.ImageField(
        _("Image"),
        upload_to=get_upload_path,
        null=True,
        blank=True,
        help_text=_("Image of the prayer"),
    )
    image_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Alt text for the image of the prayer"),
    )
    show_image = models.BooleanField(
        _("Show Image"),
        default=False,
        null=True,
        help_text=_("Set this to Yes to show image of the prayer"),
    )

    def save(self, *args, **kwargs):
        featured_prayer = super().save(*args, **kwargs)

        # Updates all other featured prayers that are featured to False
        if self.is_featured_prayer:
            Prayer.objects.exclude(id=self.id).update(is_featured_prayer=False)

        return featured_prayer

    def __str__(self):
        return f"Prayer {self.id}"

    class Meta:
        verbose_name = _("Prayer")
        verbose_name_plural = _("Prayers")
