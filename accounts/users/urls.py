from django.urls import include, path

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "token/",
        TokenObtainPairView.as_view(),
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
    ),
]