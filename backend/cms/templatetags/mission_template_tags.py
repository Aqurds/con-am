from django import template

from cms.models import Mission, MissionText, HomePageMissionTextRotate

register = template.Library()


@register.inclusion_tag("cms/tags/missions.html", takes_context=True)
def get_missions(context):
    first_mission = Mission.objects.first()
    other_missions = Mission.objects.order_by("id")[1:]
    mission_text = MissionText.objects.first()

    return {
        "first_mission": first_mission,
        "other_missions": other_missions,
        "mission_text": mission_text,
    }


@register.inclusion_tag("cms/tags/home_page_header_missions.html", takes_context=True)
def get_home_page_header_mission_texts(context):
    request = context.get("request", None)
    if request:
        header_text = HomePageMissionTextRotate.objects.values_list(
            "header_section_rotate_text", flat=True
        ).distinct()
    rotate_texts = [homepage_text for homepage_text in header_text]

    return {
        "rotate_texts": rotate_texts,
    }
