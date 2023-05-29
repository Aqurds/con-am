from functools import reduce

from django.shortcuts import get_object_or_404
from django.db.models import Q
from django import template

from cms.models import Region


register = template.Library()


@register.simple_tag()
def get_images(region):
    header_images = (
        Region.objects.get(name=region).region_images.all().order_by("?").first()
    )
    map_image = get_object_or_404(Region, name=region).header_map_image

    return {"header_images": header_images, "map_image": map_image}
