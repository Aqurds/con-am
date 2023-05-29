from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from wagtail.core import hooks
from wagtail.contrib.modeladmin.helpers import ButtonHelper
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.admin.menu import settings_menu

from wagtail.admin.wagtail_hooks import SettingsMenuItem


from cms.models import (
    Cam,
    ContactPerson,
    Region,
    SocialMedia,
    Mission,
    MissionText,
    MenuResourcePage,
    MenuExplorePage,
    MenuStrategyPage,
    SendingDistrict,
    MissionaryApi,
    MarketingAutomationSystem,
    # ContactUsModel,
    FooterSection,
)

from give.models import GivePage, SpecialGivingPage

from prayers.models import PrayerPage, Prayer

from stories.models import StoryPage

from users.models import User


class CamAdmin(ModelAdmin):
    model = Cam
    search_fields = (
        "text",
        "value",
        "type",
    )


class ContactPersonAdmin(ModelAdmin):
    model = ContactPerson
    search_fields = (
        "name",
        "email_address",
        "position",
    )


class RegionAdmin(ModelAdmin):
    model = Region
    search_fields = ("name",)
    list_display = ("name",)


class GivePageAdmin(ModelAdmin):
    model = GivePage
    search_fields = ("name",)


class PrayerAdmin(ModelAdmin):
    model = Prayer
    search_fields = ("name",)


class PrayerPageAdmin(ModelAdmin):
    model = PrayerPage
    search_fields = ("name",)


class SpecialGivingPagePageAdmin(ModelAdmin):
    menu_label = "Type of Giving Initiatives"
    model = SpecialGivingPage
    search_fields = ("name",)
    list_display = (
        "title",
        "page_type",
    )


class StoriesPageAdmin(ModelAdmin):
    menu_label = "Stories"
    model = StoryPage
    search_fields = ("name",)
    list_display = ("title", "region")


class MissionAdmin(ModelAdmin):
    model = Mission
    search_fields = ("name",)


class MissionTextAdmin(ModelAdmin):
    model = MissionText
    list_display = ("text",)


class ContentsPagesAdminGroup(ModelAdminGroup):
    menu_label = "Content"
    menu_order = 200
    items = (
        SpecialGivingPagePageAdmin,
        PrayerAdmin,
        StoriesPageAdmin,
    )


class MissionAdmin(ModelAdmin):
    model = Mission
    search_fields = ("name",)


class MissionTextAdmin(ModelAdmin):
    model = MissionText


class SendingDistrictsAdmin(ModelAdmin):
    model = SendingDistrict
    search_fields = (
        "name",
        "number",
    )


class MyButtonHelper(ButtonHelper):
    def add_button(self, classnames_add=None, classnames_exclude=None):
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []
        classnames = self.add_button_classnames + classnames_add
        cn = self.finalise_classname(classnames, classnames_exclude)
        return {
            "url": reverse("sync-to-agwm-api"),
            "label": "Sync to AGWM API",
            "classname": cn,
            "title": _("Add a new %s") % self.verbose_name,
        }


class MissionaryApiAdmin(ModelAdmin):
    model = MissionaryApi
    button_helper_class = MyButtonHelper
    menu_label = "Missionary API"
    list_display = (
        "cam_missionary_api",
        "sending_district_missionary_api",
        "region_missionary_api",
    )
    add_to_settings_menu = True


class SubPagesAdminGroup(ModelAdminGroup):
    menu_label = "Global Sections"
    menu_order = 300
    items = (
        MissionAdmin,
        ContactPersonAdmin,
        MissionTextAdmin,
    )


class MenuResourcePageAdmin(ModelAdmin):
    model = MenuResourcePage


class MenuExplorePageAdmin(ModelAdmin):
    model = MenuExplorePage


class MenuStrategyPageAdmin(ModelAdmin):
    model = MenuStrategyPage


class MenuPagesAdminGroup(ModelAdminGroup):
    menu_label = "Menu Tabs"
    menu_order = 300
    items = (
        MenuResourcePageAdmin,
        MenuExplorePageAdmin,
        MenuStrategyPageAdmin,
    )


class SocialMediaAdmin(ModelAdmin):
    model = SocialMedia
    add_to_settings_menu = True


class UserAdmin(ModelAdmin):
    model = User
    search_fields = (
        "name",
        "first_name",
        "last_name",
        "email",
        "group",
    )


class MarketingAutomationSystemAdmin(ModelAdmin):
    model = MarketingAutomationSystem
    add_to_settings_menu = True


# class ContactUsModelAdmin(ModelAdmin):
#     model = ContactUsModel
#     add_to_settings_menu = True


class FooterSectionAdmin(ModelAdmin):
    model = FooterSection
    add_to_settings_menu = True


@hooks.register("construct_main_menu")
def update_explorer_menu(request, menu_items):
    updated_menu_items = []
    for item in menu_items:
        if item.name == "reports":
            item.label = "Workflows"
        elif item.name == "settings":
            item.label = "Workflow Setup"
        updated_menu_items.append(item)

    menu_items[:] = updated_menu_items


@hooks.register("construct_settings_menu")
def update_settings_menu(request, menu_items):
    updated_settings_items = []
    for item in menu_items:
        if item.name == "locales":
            item.label = "Languages"
        updated_settings_items.append(item)

    menu_items[:] = updated_settings_items


modeladmin_register(MissionaryApiAdmin)
modeladmin_register(MarketingAutomationSystemAdmin)
modeladmin_register(MenuPagesAdminGroup)
modeladmin_register(SocialMediaAdmin)
modeladmin_register(SubPagesAdminGroup)
modeladmin_register(ContentsPagesAdminGroup)
modeladmin_register(FooterSectionAdmin)
# modeladmin_register(ContactUsModelAdmin)
