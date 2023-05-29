from django import template

from django.utils.translation import get_language

from resources.models import FeaturedResourceCenterProduct, ResourcesPage


register = template.Library()


@register.inclusion_tag("resources/tags/featured_products.html", takes_context=True)
def get_featured_products(context):
    language_code = get_language()
    featured_products = (
        FeaturedResourceCenterProduct.objects.all().order_by("-name").distinct()
    )[:3]
    featured_shop = context.get("page")
    resource_center_section_items = ResourcesPage.objects.filter(
        locale__language_code=language_code
    )

    for item in resource_center_section_items:
        resource_center = item
    return {
        "featured_products": featured_products,
        "featured_shop": featured_shop,
        "resource_center": resource_center,
    }
