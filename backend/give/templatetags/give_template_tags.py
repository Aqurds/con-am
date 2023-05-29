from django import template

from give.models import SpecialGivingIndexPage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_special_give_pages(context):
    special_give_items = None
    request = context.get("request", None)
    if request:
        special_give_items = (
            SpecialGivingIndexPage.objects.filter(
                locale__language_code=request.path.split("/")[1]
            )
            .first()
            .specific.children()
        )

    return {"special_give_items": special_give_items}
