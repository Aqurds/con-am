import base64

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from django.conf import settings
from django.db import models
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

from find_a_missionary.models import FindAMissionaryPage
from home.utils import get_upload_path, AGWMAPIService

agwm_service = AGWMAPIService()


class IndividualMissionaryPage(Page):
    """Page for each missionary"""

    about = RichTextField(
        _("About"),
        null=True,
        blank=True,
        help_text=_("About section of the page"),
    )
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
        help_text=_("Alt text for the header image of the missionary"),
    )
    header_map_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text=_("Header map image that is going to be displayed for the page"),
    )
    header_map_image_alt_text = models.CharField(
        _("Header Map Image Alt Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Alt text for the header map image of the missionary"),
    )
    content_panels = Page.content_panels + [
        FieldPanel("about"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        ImageChooserPanel("header_map_image"),
        FieldPanel("header_map_image_alt_text"),
    ]
    additional_search_fields = [
        index.SearchField("about", partial_match=True),
    ]
    search_fields = Page.search_fields + additional_search_fields


class IndividualMissionaryIndexPage(Page):
    """Index page for videos"""

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
    )
    serving_in_text = models.CharField(
        _("Serving in Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Serving in text beside individual missionary region."),
    )
    give_button_text = models.CharField(
        _("Give Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the give button."),
    )
    account_text = models.CharField(
        _("Account Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Account text next to account number."),
    )
    home_text = models.CharField(
        _("Home Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Home text next to phone number."),
    )
    about_header_text = models.CharField(
        _("About Header Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("About header text in about section."),
    )
    give_to_text = models.CharField(
        _("Give to Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Give to text next to individual missionary name in give section header."),
    )
    give_to_content = models.TextField(
        _("Give to Content"),
        null=True,
        blank=True,
        help_text=_("Give to content displayed below the give to section header."),
    )
    start_your_gift_today_button_text = models.CharField(
        _("Start Your Gift Today Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Start your gift today button text at the bottom of give to section."),
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        FieldPanel("serving_in_text"),
        FieldPanel("give_button_text"),
        FieldPanel("account_text"),
        FieldPanel("home_text"),
        FieldPanel("about_header_text"),
        FieldPanel("give_to_text"),
        FieldPanel("give_to_content"),
        FieldPanel("start_your_gift_today_button_text"),
    ]

    # Can only have InitiativesPage children
    subpage_types = ["IndividualMissionaryPage"]

    def children(self):
        return self.get_children().specific().live()

    # Handle empty individual-missionary url
    def serve(self, request, *args, **kwargs):
        code = request.GET.get("code")
        password = request.GET.get("last_name")

        if not code or not password:
            return HttpResponseRedirect(FindAMissionaryPage.objects.first().url)

        return super().serve(request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        code = request.GET.get("code")
        password = request.GET.get("last_name")

        is_sensitive_search = request.GET.get("is_sensitive_search")
        secret = settings.SECRET_KEY
        dec = []
        enc = base64.urlsafe_b64decode(code).decode()

        for i in range(len(enc)):
            key_c = secret[i % len(secret)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)

        missionary = "".join(dec)
        missionary_account_number = missionary

        # Check if safe search is true, include the password
        if is_sensitive_search:
            response = agwm_service.search(
                query=missionary_account_number, password=password
            )
        # use only the account number
        else:
            response = agwm_service.search(query=missionary_account_number)

        missionary = response.json().get("Results")[0]

        fund_guid = agwm_service.get_fund_guid(
            missionary_guid=missionary.get("ProfileGUID")
        ).json()

        context.update({"missionary": missionary, "missionary_fund_guid": fund_guid})
        return context
