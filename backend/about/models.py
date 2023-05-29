from coreapi import Field
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AboutPage(Page):
    """Model for the About Page"""

    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Image that will be shown in the header portion of the page"),
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
        help_text=_(
            "Text that will be shown in the title poriton in the header of the page"
        ),
    )
    header_content = models.TextField(
        _("Header Content"),
        null=True,
        blank=True,
        help_text=_("Text that will be shown under the header title"),
    )
    mission_content = RichTextField(
        _("Mission Content"),
        null=True,
        blank=True,
        help_text=_(
            "Content/Text that will be shown below the header portion of the page"
        ),
    )
    team_section_title = models.CharField(
        _("Team Section Header"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown in the 'Executive Team' section of the page"
        ),
    )
    world_missions_title = models.CharField(
        _("World Missions Title"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_(
            "Text that will be shown for the 'World Missions' section of the page"
        ),
    )
    world_missions_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name=_("World Missions Image"),
        help_text=_("Image that will be shown under the world missions title"),
    )
    world_missions_image_alt_text = models.CharField(
        _("World Missions Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the world missions image"),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("header_image"),
                FieldPanel("header_image_alt_text"),
                FieldPanel("header_title"),
                FieldPanel("header_content"),
            ],
            heading=_("Header Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("mission_content"),
            ],
            heading=_("Mission Content Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("team_section_title"),
                InlinePanel(
                    "executive_team_members",
                    label=_("Executive Team Member"),
                ),
            ],
            heading=_("Team Section"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("world_missions_title"),
                ImageChooserPanel("world_missions_image"),
                FieldPanel("world_missions_image_alt_text"),
            ],
            heading=_("World Missions Section"),
        ),
    ]
    additional_search_fields = [
        index.SearchField("header_title", partial_match=True),
        index.SearchField("header_content", partial_match=True),
        index.SearchField("mission_content", partial_match=True),
        index.SearchField("team_section_title", partial_match=True),
        index.SearchField("world_missions_title", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class ExecutiveTeamMember(Orderable):
    ORDER_FIRST = "first"
    ORDER_SECOND = "second"
    ORDER_OTHERS = "others"
    ORDER_CHOICES = [
        (ORDER_FIRST, "First"),
        (ORDER_SECOND, "Second"),
        (ORDER_OTHERS, "Others"),
    ]

    page = ParentalKey(
        AboutPage,
        on_delete=models.CASCADE,
        related_name="executive_team_members",
    )
    name = models.CharField(
        _("Name"),
        max_length=255,
        null=True,
        help_text=_("Name of the Executive Team member"),
    )
    position = models.CharField(
        _("Position"),
        max_length=255,
        null=True,
        help_text=_("Position of the Executive Team member"),
    )
    order = models.CharField(
        _("Order"),
        max_length=100,
        choices=ORDER_CHOICES,
        help_text=_(
            "Order in the list of team members that will be displayed. Example: Executive Director would be first etc."
        ),
    )
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Photo of the Executive Team member"),
    )
    photo_alt_text = models.CharField(
        _("Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the image"),
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("position"),
        FieldPanel("order"),
        ImageChooserPanel("photo"),
        FieldPanel("photo_alt_text"),
    ]
