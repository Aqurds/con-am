from django import template

from django.utils.translation import get_language

from videos.models import VideoIndexPage

register = template.Library()


def get_video_index_children(language_code):
    return (
        VideoIndexPage.objects.filter(locale__language_code=language_code)
        .first()
        .specific.children()
    )


@register.inclusion_tag("videos/tags/featured_video.html", takes_context=True)
def get_featured_video(context):
    featured_video = None
    request = context.get("request", None)
    if request:
        videos = get_video_index_children(language_code=request.path.split("/")[1])

    featured_video = videos.filter(videopage__is_featured=True).first()

    return {"featured_video": featured_video}


@register.inclusion_tag("videos/tags/videos.html", takes_context=True)
def get_videos(context):
    request = context.get("request", None)
    if request:
        videos = get_video_index_children(language_code=request.path.split("/")[1])

    return {"videos": videos}


@register.inclusion_tag("videos/tags/video_slider.html", takes_context=True)
def get_slider_videos(context):
    language_code = get_language()
    slider_videos = get_video_index_children(language_code=language_code)

    return {
        "slider_videos": slider_videos,
    }
