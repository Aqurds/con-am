from django import template

from give.models import SpecialGivingPage

register = template.Library()


@register.inclusion_tag("give/tags/gallery.html", takes_context=True)
def get_gallery_items(context):
    gallery_items = context.get("page").special_giving_page_images.all()
    return {"gallery_items": gallery_items}

@register.simple_tag(takes_context=True)
def get_video_items(context):
    gallery_items = context.get("page").special_giving_page_images.all().filter(is_video=True)
    return gallery_items
