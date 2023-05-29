import base64
import math

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.forms.models import AbstractFormField
from wagtail.core.models import Page
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from home.utils import AGWMAPIService, decode_string

agwm_service = AGWMAPIService()


class FindAMissionaryPage(Page):
    """Page for the find a missionary page"""

    introduction = models.TextField(
        _("Introduction"),
        help_text=_("Text to describe the page"),
        blank=True,
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
        help_text=_("Alt text for the header image of the page"),
    )
    header_text = models.CharField(
        _("Header Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Header text that is going to be displayed in the center of header image."),
    )
    search_button_text = models.CharField(
        _("Search Button Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the search button."),
    )
    search_input_placeholder_text = models.CharField(
        _("Seach Input Placeholder Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Placeholder text of the search input."),
    )
    all_region_dropdown_text = models.CharField(
        _("All Region Dropdown Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the all region dropdown tab."),
    )
    all_areas_countries_ministries_dropdown_text = models.CharField(
        _("All Areas, Countries, and Ministries Dropdown Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the all areas, countries, and ministries dropdown tab."),
    )
    areas_dropdown_text = models.CharField(
        _("Areas Dropdown Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the areas dropdown option in areas, countries, and ministries dropdown tab."),
    )
    countries_dropdown_text = models.CharField(
        _("Countries Dropdown Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the countries dropdown option in areas, countries, and ministries dropdown tab."),
    )
    ministries_dropdown_text = models.CharField(
        _("Ministries Dropdown Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the ministries dropdown option in areas, countries, and ministries dropdown tab."),
    )
    all_sending_districts_dropdown_text = models.CharField(
        _("All Sending Districts Dropdown Text"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Text of the all sending distrcits dropdown tab."),
    )
    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
        ImageChooserPanel("header_image"),
        FieldPanel("header_image_alt_text"),
        FieldPanel("header_text"),
        FieldPanel("search_button_text"),
        FieldPanel("search_input_placeholder_text"),
        FieldPanel("all_region_dropdown_text"),
        FieldPanel("all_areas_countries_ministries_dropdown_text"),
        FieldPanel("areas_dropdown_text"),
        FieldPanel("countries_dropdown_text"),
        FieldPanel("ministries_dropdown_text"),
        FieldPanel("all_sending_districts_dropdown_text"),
    ]
    additional_search_fields = [
        index.SearchField("introduction", partial_match=True, boost=2),
    ]
    search_fields = Page.search_fields + additional_search_fields

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        query = request.GET.get("query", "")
        password = request.GET.get("code", "")
        region = request.GET.get("region", "")
        cam = request.GET.get("cam", "")
        district = request.GET.get("sender", "")
        dec = []
        enc = ""
        # Try to get the page value
        page = request.GET.get("page", 1)

        if password != "false":
            enc = base64.urlsafe_b64decode(password).decode()

        dec = decode_string(enc)
        password = "".join(dec)
        response = agwm_service.search(query=query, password=password, page_number=page)

        if region:
            response = agwm_service.filter_by_region(region=region, page_number=page)
        elif cam:
            response = agwm_service.filter_by_cam(cam=cam, page_number=page)
        elif district:
            response = agwm_service.filter_by_sending_districts(
                district=district, page_number=page
            )

        results = response.json().get("Results")
        total_items = response.json().get("TotalItems")

        # Implement a list with a predetermined size
        # to pass as 1st argument in Paginator
        total_pages = math.ceil(total_items / 9)
        page_list = [None] * total_pages

        paginator = Paginator(page_list, 1)
        # since the content of the list doesnt matter in this case.
        # What only matters is the size of the list which equals the total number of pages.
        # Pass 1 as 2nd argument since the api already returns 9 items per page

        try:
            # If the page exists and is an integer
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the page is not an integer; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range then return last page of results
            posts = paginator.page(paginator.num_pages)

        context.update(
            {
                "missionaries": results,
                "total_pages": total_pages,
                "posts": posts,
            }
        )
        return context
