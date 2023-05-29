from django.http import HttpResponseRedirect
from django.urls import reverse

from cms.models import MissionaryApi
from home.utils import AGWMAPIService

agwm_service = AGWMAPIService()


def sync_to_agwm_api(request):
    if MissionaryApi.objects.first() is None:
        MissionaryApi.objects.create()

    agwm_service.get_sending_districts()
    agwm_service.get_cams()
    agwm_service.get_regions()
    return HttpResponseRedirect(reverse("cms_missionaryapi_modeladmin_index"))
