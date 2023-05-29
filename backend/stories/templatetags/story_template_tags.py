from django import template
from django.utils.translation import get_language

from cms.models import Region
from stories.models import StoryIndexPage, StorySliderHeader

register = template.Library()


@register.inclusion_tag("stories/tags/regions.html", takes_context=True)
def get_regions(context):
    regions = Region.objects.order_by("name")
    return {"regions": regions}


@register.inclusion_tag("cms/tags/generic_story_slider.html", takes_context=True)
def get_specific_stories(context):
    stories = None
    request = context.get("request", None)
    story_index_page = StoryIndexPage.objects.all()
    if request:
        stories = (
            story_index_page.filter(
                locale__language_code=get_language()
            )
            .first()
            .specific.children()
            .filter(storypage__region__name__icontains=str(context["self"]))
        )
        
    return {"stories": stories, "story_index_page": story_index_page.first()}


@register.inclusion_tag("cms/tags/generic_story_slider.html", takes_context=True)
def get_stories_for_specific_page(context):
    stories = None
    request = context.get("request", None)
    story_index_page = StoryIndexPage.objects.all()
    if request:
        stories = (
            story_index_page.filter(
                locale__language_code=get_language()
            )
            .first()
            .specific.children()
            .filter(storypage__region=context["self"].region)
            .exclude(storypage__id=context["self"].id)
        )
    return {"stories": stories, "story_index_page": story_index_page.first()}


@register.inclusion_tag("cms/tags/generic_story_slider.html", takes_context=True)
def get_stories(context):
    stories = None
    request = context.get("request", None)
    story_index_page = StoryIndexPage.objects.all()
    if request:
        stories = (
            story_index_page.filter(
                locale__language_code=get_language()
            )
            .first()
            .specific.children()
        )

    return {"stories": stories, "story_index_page": story_index_page.first()}


@register.simple_tag
def stories_slides_header():
    story_slider_headers = StorySliderHeader.objects.all()
    story_slider_dict = {
        "slider_header_text": "",
        "slider_header_text_es": "",
        "slider_subheader_text": "",
        "slider_subheader_text_es": "",
        "header_button_text": "",
        "header_button_text_es": "",
    }

    for story_slider_header in story_slider_headers:
        story_slider_dict["slider_header_text"] = story_slider_header.slider_header_text
        story_slider_dict[
            "slider_header_text_es"
        ] = story_slider_header.slider_header_text_es
        story_slider_dict[
            "slider_subheader_text"
        ] = story_slider_header.slider_subheader_text
        story_slider_dict[
            "slider_subheader_text_es"
        ] = story_slider_header.slider_subheader_text_es
        story_slider_dict[
            "header_button_text"
        ] = story_slider_header.slider_header_read_all_button
        story_slider_dict[
            "header_button_text_es"
        ] = story_slider_header.slider_header_read_all_button_es
    return story_slider_dict
