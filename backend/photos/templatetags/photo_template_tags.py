from django import template

from cms.models import Region

register = template.Library()


@register.inclusion_tag("photos/tags/regions.html", takes_context=True)
def get_regions(context):
    regions = Region.objects.all().order_by("name")
    list_tabs = []
    for region in regions:
        if region.name == "International Ministries":
            international_ministry_tab = region
        else:
            list_tabs.append(region)

    return {
        "international_ministry_tab": international_ministry_tab,
        "other_regions": list_tabs,
    }
