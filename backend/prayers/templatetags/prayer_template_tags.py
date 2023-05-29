from django import template

from prayers.models import Prayer

register = template.Library()


@register.inclusion_tag("prayers/tags/prayers.html", takes_context=True)
def get_prayers(context):
    prayers = Prayer.objects.all().order_by("id")
    return {"page": context.get("page"), "prayers": prayers}


@register.inclusion_tag("prayers/tags/featured_prayers.html", takes_context=True)
def get_featured_prayer(context):

    featured_prayer = Prayer.objects.filter(is_featured_prayer=True).first()

    return {"page": context.get("page"), "featured_prayer": featured_prayer}
