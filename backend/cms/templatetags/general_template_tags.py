from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

from about.models import AboutPage
from cms.models import (
    HomePage,
    MenuResourcePage,
    MenuExplorePage,
    MenuStrategyPage,
    GregMundisInitiative,
    MarketingAutomationSystem,
    ContactUsPage,
    FooterSection,
    FooterInformationColumn,
    FooterHomeColumn,
    FooterResourcesColumn,
    FooterExploreColumn,
    FooterStrategyColumn,
    FooterConnectColumn,
)
from give.models import GivePage, SpecialGivingIndexPage
from go.models import GoPage
from prayers.models import PrayerPage
from resources.models import ResourcesPage
from stories.models import StoryIndexPage, StoryPage
from videos.models import VideoIndexPage, VideoPage
from photos.models import PhotoIndexPage, PhotoPage
from explore_ways_to_serve.models import ExploreWaysToServe
from international_ministries.models import InternationalMinistriesPage
from regions.models import RegionPage, RegionIndexPage
from world_view.models import WorldViewIndexPage
from strategies.models import StrategyPage
from find_a_missionary.models import FindAMissionaryPage
from privacy_and_permissions.models import PrivacyPermissionsPage


def pages_dictionary(language_code):
    return {
        "home": HomePage.objects.filter(locale__language_code=language_code).first(),
        "pray": PrayerPage.objects.filter(locale__language_code=language_code).first(),
        "give": GivePage.objects.filter(locale__language_code=language_code).first(),
        "go": GoPage.objects.filter(locale__language_code=language_code).first(),
        "greg_mundis_initiative": GregMundisInitiative.objects.filter(
            locale__language_code=language_code
        ).first(),
        "resources": ResourcesPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "stories": StoryIndexPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "videos": VideoIndexPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "photos": PhotoIndexPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "explore": ExploreWaysToServe.objects.filter(
            locale__language_code=language_code
        ).first(),
        "international_ministries": InternationalMinistriesPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "world_views": WorldViewIndexPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "strategy": StrategyPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "regions": RegionIndexPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "about": AboutPage.objects.filter(locale__language_code=language_code).first(),
        "find_a_missionary": FindAMissionaryPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "special_give": SpecialGivingIndexPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "privacy_permission": PrivacyPermissionsPage.objects.filter(
            locale__language_code=language_code
        ).first(),
        "contact_us": ContactUsPage.objects.filter(
            locale__language_code=language_code
        ).first(),
    }


register = template.Library()


@register.simple_tag(takes_context=True)
def get_page(context, page):
    language_code = context.request.LANGUAGE_CODE
    return pages_dictionary(language_code).get(page)


@register.simple_tag()
def get_resource_pages():
    return MenuResourcePage.objects.order_by("id")


@register.simple_tag()
def get_explore_pages():
    return MenuExplorePage.objects.order_by("id")


@register.simple_tag()
def get_strategy_pages():
    return MenuStrategyPage.objects.order_by("id")


@register.simple_tag(takes_context=True)
def get_region_page(context, region):
    request = context.get("request", None)
    return RegionPage.objects.filter(
        title=region, locale__language_code=request.path.split("/")[1]
    ).first()


@register.simple_tag()
def get_marketing_automation_system():
    return MarketingAutomationSystem.objects.all()


@register.simple_tag()
def get_footer_section_buttons():
    return FooterSection.objects.all()


@register.simple_tag()
def get_footer_section_information_buttons():
    return FooterInformationColumn.objects.latest("id")


@register.simple_tag()
def get_footer_section_home_buttons():
    home_buttons = FooterHomeColumn.objects.all()
    list_pages = []
    for button in home_buttons:
        if button.is_top_link:
            first_text = button
        else:
            list_pages.append(button)
    return {"first_text": first_text, "other_texts": list_pages}


@register.simple_tag()
def get_footer_section_resources_buttons():
    resources_buttons = FooterResourcesColumn.objects.exclude(name="Merchandise")
    merchandise_button = FooterResourcesColumn.objects.filter(
        name="Merchandise"
    ).first()
    list_pages = []
    for button in resources_buttons:
        if button.is_top_link:
            first_text = button
        else:
            list_pages.append(button)
    return {
        "first_text": first_text,
        "other_texts": list_pages,
        "merchandise": merchandise_button,
    }


@register.simple_tag()
def get_footer_section_explore_buttons():
    explore_buttons = FooterExploreColumn.objects.order_by("name").exclude(
        name="International Ministries"
    )
    ministries_button = FooterExploreColumn.objects.filter(
        name="International Ministries"
    ).first()
    list_pages = []
    for button in explore_buttons:
        if button.is_top_link:
            first_text = button
        else:
            list_pages.append(button)
    return {
        "first_text": first_text,
        "other_texts": list_pages,
        "ministries_button": ministries_button,
    }


@register.simple_tag()
def get_footer_section_strategy_buttons():
    strategy_buttons = FooterStrategyColumn.objects.all()
    list_pages = []
    for button in strategy_buttons:
        if button.is_top_link:
            first_text = button
        else:
            list_pages.append(button)
    return {"first_text": first_text, "other_texts": list_pages}


@register.simple_tag()
def get_footer_section_connect_buttons():
    connect_buttons = FooterConnectColumn.objects.latest("id")
    list_pages = []
    if connect_buttons.is_top_link:
        first_text = connect_buttons
    else:
        list_pages.append(connect_buttons)

    return {"first_text": first_text, "other_texts": list_pages}


@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr, "")


@register.filter
def highlight_search(text, search):
    highlighted_text = text.replace(
        search, "<span class='text-[#8B3C3A]'>{}</span>".format(search)
    )
    return mark_safe(highlighted_text)


@register.simple_tag()
def get_resource_items():
    language_code = get_language()
    first_story = StoryPage.objects.filter(locale__language_code=language_code).first()

    first_photo = PhotoPage.objects.filter(locale__language_code=language_code).first()

    first_video = VideoPage.objects.filter(locale__language_code=language_code).first()

    return {
        "first_story": first_story,
        "first_photo": first_photo,
        "first_video": first_video,
    }


@register.simple_tag()
def get_world_views_pages():
    language_code = get_language()
    world_view_items = (
        WorldViewIndexPage.objects.filter(locale__language_code=language_code)
        .first()
        .specific.children()
    )

    return {"world_view_items": world_view_items}


@register.simple_tag()
def get_notification_setting_text():
    language_code = get_language()
    notification_items = HomePage.objects.filter(locale__language_code=language_code)
    for item in notification_items:
        notification_text = item

    return {"notification_text": notification_text}
    