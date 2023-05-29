from django import template

register = template.Library()


@register.inclusion_tag("go/tags/gallery.html", takes_context=True)
def get_gallery_items(context):
    gallery_items = context.get("page").go_gallery.all()
    return {"gallery_items": gallery_items}


@register.simple_tag(takes_context=True)
def get_video_items(context):
    gallery_items = context.get("page").go_gallery.all().filter(is_video=True)
    return gallery_items
