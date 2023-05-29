"""agwm_31244 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from allauth.account.views import confirm_email
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from find_a_missionary import views as search_views
from cms import views as search_page_views

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("modules/", include("modules.urls")),
    path("api/v1/", include("home.api.v1.urls")),
    path("django-admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path(
        "redirect_to_missionary_page/<str:account_number>/<str:last_name>/",
        search_views.redirect_to_missionary_page,
        name="individual-missionary",
    ),
    path(
        "redirect_to_find_a_missionary_page_filter_by_region/<str:region>/",
        search_views.redirect_to_find_a_missionary_page_filter_by_region,
        name="find-a-missionary-filter-by-region",
    ),
    path(
        "redirect_to_find_a_missionary_page_filter_by_cam/<str:cam>/",
        search_views.redirect_to_find_a_missionary_page_filter_by_cam,
        name="find-a-missionary-cam",
    ),
    path(
        "redirect_to_find_a_missionary_page_filter_by_sending_districts/<str:district>/",
        search_views.redirect_to_find_a_missionary_page_filter_by_sending_districts,
        name="find-a-missionary-sending-districts",
    ),
    path(
        "htmx/search-missionary/<initial_argument>",
        search_views.search_missionary,
        name="search-missionary",
    ),
    path("search/", search_page_views.search, name="search"),
    # path(
    #     "contact-us/",
    #     search_page_views.ContactUsFormCreateView.as_view(),
    #     name="contact-us-page",
    # ),
    path("rest-auth/", include("rest_auth.urls")),
    # Override email confirm to use allauth's HTML view instead of rest_auth's API view
    path("rest-auth/registration/account-confirm-email/<str:key>/", confirm_email),
    path(
        "rest-auth/registration/",
        include("rest_auth.registration.urls"),
    ),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
]

admin.site.site_header = "AGWM"
admin.site.site_title = "AGWM Admin Portal"
admin.site.index_title = "AGWM Admin"

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# swagger
api_info = openapi.Info(
    title="AGWM API",
    default_version="v1",
    description="API documentation for AGWM App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]


urlpatterns += i18n_patterns(
    path("", include(wagtail_urls)),
)
