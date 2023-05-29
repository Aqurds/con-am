from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class LegacyPage(Page):
    legacy_giving_header = models.CharField(
        _("Legacy Giving Header"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Title that will be shown in the header portion of the page"),
    )
    legacy_giving_header_body = models.CharField(
        _("Header Body"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            "Text that will be shown in the body portion in the header of the page"
        ),
    )
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be displayed in the header section of the page"),
    )
    header_image_alt_text = models.CharField(
        _("Header Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header image"),
    )
    header_give_now_button_text = models.CharField(
        _("Header Give Now Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Give now button text in the header."),
    )
    legacy_content_title = models.CharField(
        _("Legacy Content Title"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Title the will be shown in the content portion of the page"),
    )
    legacy_content_body = RichTextField(
        _("Legacy Content Body"),
        null=True,
        blank=True,
        help_text=_(
            "Content of the body that will be shown in the content portion of the page"
        ),
    )
    methods_of_planned_giving_header_text = models.CharField(
        _("Methods of Planned Giving Header Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in the header of methods of plannged giving section."),
    )
    methods_of_planned_giving_box_1_text = models.CharField(
        _("Methods of Planned Giving Box 1 Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in first box of Methods of Planned Giving section."),
    )
    methods_of_planned_giving_box_2_text = models.CharField(
        _("Methods of Planned Giving Box 2 Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in second box of Methods of Planned Giving section."),
    )
    methods_of_planned_giving_box_3_text = models.CharField(
        _("Methods of Planned Giving Box 3 Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in third box of Methods of Planned Giving section."),
    )
    methods_of_planned_giving_box_4_text = models.CharField(
        _("Methods of Planned Giving Box 4 Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in fourth box of Methods of Planned Giving section."),
    )
    methods_of_planned_giving_box_5_text = models.CharField(
        _("Methods of Planned Giving Box 5 Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in fifth box of Methods of Planned Giving section."),
    )
    methods_of_planned_giving_box_6_text = models.CharField(
        _("Methods of Planned Giving Box 6 Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in last box of Methods of Planned Giving section."),
    )
    start_giving_section_header = models.CharField(
        _("Start Giving Section Header Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in header of Start Giving Section."),
    )
    start_giving_section_content = models.TextField(
        _("Start Giving Section Content"),
        blank=True,
        null=True,
        help_text=_("Text that will be shown in content of Start Giving Section."),
    )
    start_giving_section_button_text = models.CharField(
        _("Start Giving Section Button Text"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Text that will be shown in button of Start Giving Section."),
    )
    content_panels = Page.content_panels + [
        FieldPanel("legacy_giving_header"),
        FieldPanel("legacy_giving_header_body"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("header_give_now_button_text"),
        FieldPanel("legacy_content_title"),
        FieldPanel("legacy_content_body"),
        FieldPanel("methods_of_planned_giving_header_text"),
        FieldPanel("methods_of_planned_giving_box_1_text"),
        FieldPanel("methods_of_planned_giving_box_2_text"),
        FieldPanel("methods_of_planned_giving_box_3_text"),
        FieldPanel("methods_of_planned_giving_box_4_text"),
        FieldPanel("methods_of_planned_giving_box_5_text"),
        FieldPanel("methods_of_planned_giving_box_6_text"),
        FieldPanel("start_giving_section_header"),
        FieldPanel("start_giving_section_content"),
        FieldPanel("start_giving_section_button_text"),
    ]

    additional_search_fields = [
        index.SearchField("legacy_giving_header", partial_match=True),
        index.SearchField("legacy_giving_header_body", partial_match=True),
        index.SearchField("legacy_content_title", partial_match=True),
        index.SearchField("legacy_content_body", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields

    class Meta:
        verbose_name = _("Legacy Page")
        verbose_name_plural = _("Legay Pages")
