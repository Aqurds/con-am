from django.conf import settings
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query

from about.models import AboutPage
from cms.models import HomePage, GregMundisInitiative
from explore_ways_to_serve.models import ExploreWaysToServe
from faq.models import FaqPage
from find_a_missionary.models import FindAMissionaryPage
from give.models import GivePage, SpecialGivingPage
from go.models import GoPage
from individual_missionaries.models import IndividualMissionaryPage
from initiatives.models import InitiativesPage, InitiativeIndexPage
from international_ministries.models import (
    IndividualMinistryPage,
    InternationalMinistriesPage,
)
from legacy.models import LegacyPage
from missionaries.models import MissionaryPage
from prayers.models import PrayerPage
from regions.models import RegionPage, RegionIndexPage
from resources.models import ResourcesPage
from stories.models import StoryPage
from strategies.models import StrategyPage
from videos.models import VideoPage

def search(request):
    search_query = request.GET.get("query", None)
    lang = request.GET.get("lang", None)
    language_code = lang if lang is not None else "en"

    if search_query:
        about_page_results = AboutPage.objects.live().search(search_query)
        about_page_ids = [p.page_ptr.id for p in about_page_results]

        explore_ways_to_serve_result = ExploreWaysToServe.objects.live().search(
            search_query
        )
        explore_ways_to_serve_ids = [
            p.page_ptr.id for p in explore_ways_to_serve_result
        ]

        faq_page_results = FaqPage.objects.live().search(search_query)
        faq_page_ids = [p.page_ptr.id for p in faq_page_results]

        find_a_missionary_page_results = FindAMissionaryPage.objects.live().search(
            search_query
        )
        find_a_missionary_page_ids = [
            p.page_ptr.id for p in find_a_missionary_page_results
        ]

        give_page_results = GivePage.objects.live().search(search_query)
        give_page_ids = [p.page_ptr.id for p in give_page_results]

        go_page_results = GoPage.objects.live().search(search_query)
        go_page_ids = [p.page_ptr.id for p in go_page_results]

        greg_mundis_initiative_page_results = (
            GregMundisInitiative.objects.live().search(search_query)
        )
        greg_mundis_intiative_page_ids = [
            p.page_ptr.id for p in greg_mundis_initiative_page_results
        ]

        special_give_page_results = SpecialGivingPage.objects.live().search(
            search_query
        )
        special_give_page_ids = [p.page_ptr.id for p in special_give_page_results]

        home_page_results = HomePage.objects.live().search(search_query)
        home_page_ids = [p.page_ptr.id for p in home_page_results]

        individual_missionary_page_results = (
            IndividualMissionaryPage.objects.live().search(search_query)
        )
        individual_missionary_page_ids = [
            p.page_ptr.id for p in individual_missionary_page_results
        ]

        initiatives_page_results = InitiativesPage.objects.live().search(search_query)
        initiatives_page_ids = [p.page_ptr.id for p in initiatives_page_results]

        initiative_index_page_results = InitiativeIndexPage.objects.live().search(
            search_query
        )
        initiative_index_page_ids = [
            p.page_ptr.id for p in initiative_index_page_results
        ]

        individual_ministry_page_results = IndividualMinistryPage.objects.live().search(
            search_query
        )
        individual_ministry_page_ids = [
            p.page_ptr.id for p in individual_ministry_page_results
        ]

        international_ministry_page_results = (
            InternationalMinistriesPage.objects.live().search(search_query)
        )
        international_ministry_page_ids = [
            p.page_ptr.id for p in international_ministry_page_results
        ]

        legacy_page_results = LegacyPage.objects.live().search(search_query)
        legacy_page_ids = [p.page_ptr.id for p in legacy_page_results]

        missionary_page_results = MissionaryPage.objects.live().search(search_query)
        missionary_page_ids = [p.page_ptr.id for p in missionary_page_results]

        prayers_page_results = PrayerPage.objects.live().search(search_query)
        prayers_page_ids = [p.page_ptr.id for p in prayers_page_results]

        region_page_results = RegionPage.objects.live().search(search_query)
        region_page_ids = [p.page_ptr.id for p in region_page_results]

        region_index_page_results = RegionIndexPage.objects.live().search(search_query)
        region_index_page_ids = [p.page_ptr.id for p in region_index_page_results]

        resources_page_results = ResourcesPage.objects.live().search(search_query)
        resources_page_ids = [p.page_ptr.id for p in resources_page_results]

        stories_page_results = StoryPage.objects.live().search(search_query)
        stories_page_ids = [p.page_ptr.id for p in stories_page_results]

        strategies_page_results = StrategyPage.objects.live().search(search_query)
        strategies_page_ids = [p.page_ptr.id for p in strategies_page_results]

        videos_page_results = VideoPage.objects.live().search(search_query)
        videos_page_ids = [p.page_ptr.id for p in videos_page_results]

        page_ids = (
            about_page_ids
            + home_page_ids
            + greg_mundis_intiative_page_ids
            + explore_ways_to_serve_ids
            + faq_page_ids
            + find_a_missionary_page_ids
            + give_page_ids
            + go_page_ids
            + special_give_page_ids
            + individual_missionary_page_ids
            + initiatives_page_ids
            + initiative_index_page_ids
            + individual_ministry_page_ids
            + international_ministry_page_ids
            + legacy_page_ids
            + missionary_page_ids
            + prayers_page_ids
            + region_page_ids
            + region_index_page_ids
            + resources_page_ids
            + stories_page_ids
            + strategies_page_ids
            + videos_page_ids
        )
        
        search_results = Page.objects.live().filter(
            id__in=page_ids, locale__language_code=language_code
        )

        query = Query.get(search_query)

        # Record hit
        query.add_hit()

    else:
        search_results = Page.objects.none()

    language_list = [lang[0] for lang in settings.LANGUAGES]
    language_list.remove(language_code)

    return render(
        request,
        "search/search_page_results.html",
        {
            "for_search": True,
            "search_query": search_query,
            "search_results": search_results,
            "current_language": language_code,
            "other_language": language_list,
        },
    )


# class ContactUsFormCreateView(CreateView):
#     model = ContactUsModel
#     template_name = "cms/contact_us_page.html"
#     success_url = reverse_lazy("contact-us-page")
#     form_class = ContactUsSendEmailForm

#     def get_success_url(self):
#         language_code = get_language()
#         return (
#             ContactUsPage.objects.filter(locale__language_code=language_code)
#             .first()
#             .url
#         )

#     def get_form_kwargs(self):
#         form_kwargs = super().get_form_kwargs()
#         form_kwargs.update({"request": self.request})

#         return form_kwargs
