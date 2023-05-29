from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.db import models
from django.utils.translation import ugettext_lazy as _


class MissionaryPage(Page):
    """Page for a specific missionary"""

    name = models.CharField(
        _("Name"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Name of missionary"),
    )
    location = models.CharField(
        _("Location"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Location of the missionary"),
    )
    account_number = models.CharField(
        _("Account Number"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Account number of the missionary"),
    )
    email_address = models.EmailField(
        _("Email Address"),
        null=True,
        blank=True,
        max_length=100,
        help_text=_("Email address of the missionary"),
    )
    website = models.CharField(
        _("Website"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Website of the missionary"),
    )
    facebook_url = models.CharField(
        _("Facebook URL"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Facebook URL of the missionary"),
    )
    instagram_url = models.CharField(
        _("Instagram URL"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Instagram URL of the missionary"),
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("World view image"),
        verbose_name=_("Image"),
    )
    about = RichTextField(
        _("About"),
        null=True,
        blank=True,
        help_text=_("About area/text of the missionary"),
    )

    giving_initiative_header = models.CharField(
        _("Giving Initiative Header"),
        max_length=100,
        null=True,
        blank=True,
        help_text=_("Header for the Giving Initiative section"),
    )
    giving_initiative_body = models.TextField(
        _("Giving Initiative Body"),
        null=True,
        blank=True,
        help_text=_("Body for the Giving Initiative section"),
    )
    giving_initiative_goal = models.IntegerField()
    giving_initiative_current_amount = models.IntegerField()

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("location"),
        FieldPanel("account_number"),
        FieldPanel("email_address"),
        FieldPanel("website"),
        FieldPanel("facebook_url"),
        FieldPanel("instagram_url"),
        ImageChooserPanel("image"),
        FieldPanel("about"),
        FieldPanel("giving_initiative_header"),
        FieldPanel("giving_initiative_body"),
        FieldPanel("giving_initiative_goal"),
        FieldPanel("giving_initiative_current_amount"),
    ]

    additional_search_fields = [
        index.SearchField("name", partial_match=True),
        index.SearchField("location", partial_match=True),
        index.SearchField("account_number", partial_match=True),
        index.SearchField("email_address", partial_match=True),
        index.SearchField("website", partial_match=True),
        index.SearchField("facebook_url", partial_match=True),
        index.SearchField("instagram_url", partial_match=True),
        index.SearchField("about", partial_match=True),
        index.SearchField("giving_initiative_header", partial_match=True),
        index.SearchField("giving_initiative_body", partial_match=True),
        index.SearchField("giving_initiative_goal", partial_match=True),
        index.SearchField("giving_initiative_current_amount", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class MissionaryIndexPage(Page):
    """Index page for Missionaries"""

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["MissionaryPage"]

    def children(self):
        return self.get_children().specific().live()
