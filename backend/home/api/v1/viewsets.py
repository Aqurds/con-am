from django.shortcuts import get_object_or_404

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    CategorySerializer,
    UserNotificationSerializer,
)

from home.models import *
from users.models import User


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class UserNotificationUpdateAPIView(UpdateAPIView):
    serializer_class = UserNotificationSerializer
    queryset = User.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.queryset, id=self.request.user.id)

        return obj


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CategoryViewSet(ViewSet):

    serializer_class = CategorySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise serializers.ValidationError(
                {"success": "false", "error": "Category does not exist"}
            )

    def list(self, request):
        queryset = Category.objects.filter()
        serializer = CategorySerializer(queryset, many=True)
        return Response({"success": True, "response": serializer.data})
