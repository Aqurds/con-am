from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    CategoryViewSet,
    UserNotificationUpdateAPIView,
)

from home.api.v1.views import sync_to_agwm_api

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "user-notification",
        UserNotificationUpdateAPIView.as_view(),
        name="update-user-notification",
    ),
    path(
        "sync_to_agwm_api/",
        sync_to_agwm_api,
        name="sync-to-agwm-api",
    ),
]
