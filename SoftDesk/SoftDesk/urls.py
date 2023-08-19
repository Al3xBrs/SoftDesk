"""
URL configuration for SoftDesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Users.views import RegisterView, getProfile, updateProfile
from Projects.views import ProjectRegisterView
from Projects.urls import router as projects_router

router = routers.DefaultRouter()
router.registry.extend(projects_router.registry)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api/", include(router.urls), name="api_home"),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/register/", RegisterView.as_view(), name="auth_register"),
    path(
        "api/register/project/", ProjectRegisterView.as_view(), name="project_register"
    ),
    path("api/profile/", getProfile, name="profile"),
    path("api/profile/update/", updateProfile, name="update-profile"),
]
