from django import template
from about.models import ExecutiveTeamMember

register = template.Library()


@register.simple_tag(takes_context=True)
def get_first_team_member(context):
    return (
        context.get("page")
        .executive_team_members.filter(order=ExecutiveTeamMember.ORDER_FIRST)
        .first()
    )


@register.simple_tag(takes_context=True)
def get_second_team_member(context):
    return (
        context.get("page")
        .executive_team_members.filter(order=ExecutiveTeamMember.ORDER_SECOND)
        .first()
    )


@register.simple_tag(takes_context=True)
def get_other_team_members(context):
    return (
        context.get("page")
        .executive_team_members.filter(order=ExecutiveTeamMember.ORDER_OTHERS)
        .all()
    )
