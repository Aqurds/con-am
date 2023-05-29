from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from django.db import models
from django.utils.translation import ugettext_lazy as _

from home.utils import get_upload_path


class FaqPage(Page):
    """Page for the FAQ"""

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

    contributions_faq_text = models.CharField(
        _("Contribution FAQ Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Contribution faq text shown in dropdown."),
    )

    contributions_faq = RichTextField(
        _("contributions_faq"),
        null=True,
        blank=True,
        help_text=_("Content under the contributions faq section"),
    )

    online_commitment_forms_text = models.CharField(
        _("Online Commitment Forms Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Online commitment forms text shown in dropdown."),
    )

    online_commitment_forms = RichTextField(
        _("Online Commitment Forms"),
        null=True,
        blank=True,
        help_text=_("Content under the online commitment forms section"),
    )

    downloadable_commitment_forms_text = models.CharField(
        _("Downloadable Commitment Forms Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Downloadable commitment forms text shown in dropdown."),
    )

    downloadable_commitment_forms = RichTextField(
        _("Downloadable Commitment Forms"),
        null=True,
        blank=True,
        help_text=_("Content under the downloadable commitment forms section"),
    )

    other_online_contributions_text = models.CharField(
        _("Other Online Contribution Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Other online contribution text shown in dropdown."),
    )

    other_online_contributions = RichTextField(
        _("Other Online Contributions"),
        null=True,
        blank=True,
        help_text=_("Content under the other online contributions section"),
    )

    automatic_monthly_contributions_text = models.CharField(
        _("Automatic Monthly Contribution Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Automatic monthly contribution text shown in dropdown."),
    )

    automatic_monthly_contributions = RichTextField(
        _("Automatic Monthly Contributions"),
        null=True,
        blank=True,
        help_text=_("Content under the automatic monthly contributions section"),
    )

    claiming_world_missions_ministries_credit_text = models.CharField(
        _("Claiming World Missions Ministries Credit Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Claiming world missions ministries credit text shown in dropdown."),
    )

    claiming_world_missions_ministries_credit = RichTextField(
        _("Claiming World Missions Ministries Credit"),
        null=True,
        blank=True,
        help_text=_(
            "Content under the claiming world missions ministries credit section"
        ),
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [ImageChooserPanel("header_image"), FieldPanel("header_image_alt_text")],
            heading=_("Header Section"),
        ),
        FieldPanel("contributions_faq_text"),
        FieldPanel("contributions_faq"),
        FieldPanel("online_commitment_forms_text"),
        FieldPanel("online_commitment_forms"),
        FieldPanel("downloadable_commitment_forms_text"),
        FieldPanel("downloadable_commitment_forms"),
        FieldPanel("other_online_contributions_text"),
        FieldPanel("other_online_contributions"),
        FieldPanel("automatic_monthly_contributions_text"),
        FieldPanel("automatic_monthly_contributions"),
        FieldPanel("claiming_world_missions_ministries_credit_text"),
        FieldPanel("claiming_world_missions_ministries_credit"),
    ]
    additional_search_fields = [
        index.SearchField("contributions_faq", partial_match=True),
        index.SearchField("online_commitment_forms", partial_match=True),
        index.SearchField("downloadable_commitment_forms", partial_match=True),
        index.SearchField("other_online_contributions", partial_match=True),
        index.SearchField("automatic_monthly_contributions", partial_match=True),
        index.SearchField(
            "claiming_world_missions_ministries_credit", partial_match=True
        ),
    ]
    search_fields = Page.search_fields + additional_search_fields
