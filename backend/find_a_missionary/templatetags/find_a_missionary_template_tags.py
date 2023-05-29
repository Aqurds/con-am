from django import template

from cms.models import Cam, Region, SendingDistrict

register = template.Library()


@register.simple_tag(takes_context=True)
def get_regions(context):
    regions = Region.objects.order_by("name")
    return regions


@register.simple_tag(takes_context=True)
def get_cam(context, type):
    cam = Cam.objects.filter(type=type).order_by("text")
    return cam


@register.simple_tag(takes_context=True)
def get_sending_districts(context):
    district = SendingDistrict.objects.order_by("name")
    return district


@register.simple_tag(takes_context=True)
def get_page_parameters(context, params, is_page_number):
    key2 = ""
    value2 = ""
    if is_page_number:
        return params.get("page")
    else:
        for key, value in params.items():
            if key != "code":
                key2 = key
                value2 = value

    return f"&{key2}={value2}"
