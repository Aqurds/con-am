from django import template

register = template.Library()


@register.inclusion_tag("privacy_and_permissions/tags/content.html", takes_context=True)
def get_privacy_permissions_content(context):
    content = context.get("page").privacy_permission_page_content.all()
    return {"content_items": content}
