from django.contrib import admin

from cms.models import (
    Region,
    SendingDistrict,
    Cam,
    MissionaryApi,
    MarketingAutomationSystem,
    ContactUsModel,
)

admin.site.register(Region)
admin.site.register(SendingDistrict)
admin.site.register(Cam)
admin.site.register(MissionaryApi)
admin.site.register(MarketingAutomationSystem)
admin.site.register(ContactUsModel)
