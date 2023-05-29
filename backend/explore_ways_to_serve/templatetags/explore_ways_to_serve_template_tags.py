from django import template


register = template.Library()


@register.inclusion_tag(
    "explore_ways_to_serve/tags/qualifications.html", takes_context=True
)
def get_qualifications(context, tab, section):
    qualifications = None
    if tab == "short-term":
        if section == "first_section":
            qualifications = context.get(
                "page"
            ).short_term_first_tab_qualification.all()
        elif section == "second_section":
            qualifications = context.get(
                "page"
            ).short_term_second_tab_qualification.all()
        else:
            qualifications = context.get(
                "page"
            ).short_term_third_tab_qualification.all()
    elif tab == "1-2-year":
        qualifications = context.get("page").one_to_two_year_qualification.all()
    else:
        qualifications = context.get("page").career_qualification.all()

    return {"qualifications": qualifications}


@register.inclusion_tag(
    "explore_ways_to_serve/tags/application_processes.html", takes_context=True
)
def get_application_processes(context, section):
    application_processes = None
    last_application_process = None
    if section == "1-2-year":
        last_number = context.get("page").one_to_two_year_application_process.count()

        last_application_process = context.get(
            "page"
        ).one_to_two_year_application_process.latest("id")
        application_processes = context.get(
            "page"
        ).one_to_two_year_application_process.exclude(id=last_application_process.id)
    else:
        last_number = last_number = context.get(
            "page"
        ).career_application_process.count()
        last_application_process = context.get(
            "page"
        ).career_application_process.latest("id")
        application_processes = context.get("page").career_application_process.exclude(
            id=last_application_process.id
        )

    return {
        "application_processes": application_processes,
        "last_application_process": last_application_process,
        "last_number": last_number,
    }


@register.inclusion_tag("explore_ways_to_serve/tags/gallery.html", takes_context=True)
def get_gallery(context, section):
    if section == "1_2_year":
        gallery_items = context.get("page").one_to_two_year_gallery.all()
    else:
        gallery_items = context.get("page").career_gallery.all()

    return {"gallery_items": gallery_items, "section": section}


@register.simple_tag(takes_context=True)
def get_video_items(context, section):
    if section == "1_2_year":
        gallery_items = (
            context.get("page").one_to_two_year_gallery.all().filter(is_video=True)
        )
    else:
        gallery_items = context.get("page").career_gallery.all().filter(is_video=True)
    return gallery_items

@register.filter()
def email_for_button(email):
    return "Email " + email