from django import template

from give.models import SpecialGivingPage, GivePage

register = template.Library()


@register.inclusion_tag("cms/tags/greg_mundis_initiatives.html", takes_context=True)
def get_initiatives(context):
    request = context.get("request", None)
    if request:
        greg_mundis_initiatives = SpecialGivingPage.objects.filter(
            page_type=SpecialGivingPage.TYPE_EXECUTIVE,
            locale__language_code=request.path.split("/")[1],
        )

    return {
        "greg_mundis_initiatives": greg_mundis_initiatives,
        "give_page": GivePage.objects.first(),
    }
