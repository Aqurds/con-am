from django import template

from django.utils.translation import get_language

from cms.models import HomePageImages

from regions.models import RegionIndexPage

register = template.Library()

@register.inclusion_tag(
    "cms/tags/home_page_header_background_images.html", takes_context=True
)
def get_home_page_images(context):
    header_section_images = HomePageImages.objects.all()
    image_file_paths = [
        homepage_image.header_image.url for homepage_image in header_section_images
    ]
    return {"first_image_file_path": image_file_paths[0], "other_image_file_paths": image_file_paths[1:]}


@register.simple_tag()
def get_regions_slider_pages():
    regions_slider_items = None
    language_code = get_language()
    regions_slider_items = (
        RegionIndexPage.objects.filter(locale__language_code=language_code)
        .first()
        .specific.children()
    )

    return {"regions_slider_items": regions_slider_items}
