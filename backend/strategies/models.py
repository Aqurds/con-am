from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class StrategyPage(Page):
    """Page for the Strategies"""

    # Header section
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Header image of the page"),
        verbose_name=_("Header Image"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    header_title = models.CharField(
        _("Header Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text that will be shown in the header porition of the page"),
    )
    header_body = models.TextField(
        _("Header Body"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the header"),
    )

    header_button_reaching = models.CharField(
        _("Reaching Header Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Reaching button in the header section"),
    )

    header_button_planting = models.CharField(
        _("Planting Header Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Planting button in the header section"),
    )

    header_button_training = models.CharField(
        _("Training Header Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Training button in the header section"),
    )

    header_button_serving = models.CharField(
        _("Serving Header Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Serving button in the header section"),
    )

    # Reaching Section
    reaching_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Background image of the reaching section"),
        verbose_name=_("Reaching Background Image"),
    )
    reaching_background_image_alt_text = models.CharField(
        _("Reaching Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the reaching background image"),
    )
    reaching_title = models.CharField(
        _("Reaching Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the reaching section"),
    )
    reaching_body = models.TextField(
        _("Reaching Body"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the reaching title"),
    )

    # Planting Section
    planting_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Background image of the planting section"),
        verbose_name=_("Planting Background Image"),
    )
    planting_background_image_alt_text = models.CharField(
        _("Planting Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the planting background image"),
    )
    planting_title = models.CharField(
        _("Planting Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the planting section"),
    )
    planting_body = models.TextField(
        _("Planting Body"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the planting title"),
    )

    # Training Section
    training_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Background Image of the training section"),
        verbose_name=_("Training Background Image"),
    )
    training_background_image_alt_text = models.CharField(
        _("Training Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the training background image"),
    )
    training_title = models.CharField(
        _("Training Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the Training section"),
    )
    training_body = models.TextField(
        _("Training Body"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the Training title"),
    )

    # Serving Section
    serving_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Background image of the serving section"),
        verbose_name=_("Serving Background Image"),
    )
    serving_background_image_alt_text = models.CharField(
        _("Serving Background Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the serving background image"),
    )
    serving_title = models.CharField(
        _("Serving Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Title text for the Serving section"),
    )
    serving_body = models.TextField(
        _("Serving Body"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the Serving title"),
    )

    cta_pray_button = models.CharField(
        _("CTA Pray Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Pray button in the CTA section"),
    )

    cta_give_button = models.CharField(
        _("CTA Give Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Give button in the CTA section"),
    )

    cta_go_button = models.CharField(
        _("CTA Go Button Text"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Text of the Go button in the CTA section"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                FieldPanel("header_title"),
                FieldPanel("header_body"),
            ],
            heading=_("Header Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("reaching_background_image"),
                FieldPanel("reaching_background_image_alt_text"),
                FieldPanel("reaching_title"),
                FieldPanel("reaching_body"),
            ],
            heading=_("Reaching Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("planting_background_image"),
                FieldPanel("planting_background_image_alt_text"),
                FieldPanel("planting_title"),
                FieldPanel("planting_body"),
            ],
            heading=_("Planting Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("training_background_image"),
                FieldPanel("training_background_image_alt_text"),
                FieldPanel("training_title"),
                FieldPanel("training_body"),
            ],
            heading=_("Training Section"),
        ),
        MultiFieldPanel(
            [
                ImageChooserPanel("serving_background_image"),
                FieldPanel("serving_background_image_alt_text"),
                FieldPanel("serving_title"),
                FieldPanel("serving_body"),
            ],
            heading=_("Serving Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("header_button_reaching"),
                FieldPanel("header_button_planting"),
                FieldPanel("header_button_training"),
                FieldPanel("header_button_serving"),
                FieldPanel("cta_pray_button"),
                FieldPanel("cta_give_button"),
                FieldPanel("cta_go_button"),
            ],
            heading=_("Translatable Strategy Page Buttons and Text fields"),
        ),
    ]

    additional_search_fields = [
        index.SearchField("header_title", partial_match=True),
        index.SearchField("header_body", partial_match=True),
        index.SearchField("reaching_title", partial_match=True),
        index.SearchField("reaching_body", partial_match=True),
        index.SearchField("planting_title", partial_match=True),
        index.SearchField("planting_body", partial_match=True),
        index.SearchField("training_title", partial_match=True),
        index.SearchField("training_body", partial_match=True),
        index.SearchField("serving_title", partial_match=True),
        index.SearchField("serving_body", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields
