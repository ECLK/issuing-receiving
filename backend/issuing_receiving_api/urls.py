"""issuing_receiving_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .authentication import BearerAuthentication
schema_view = get_schema_view(
    openapi.Info(
        title="Issuing Receiving API",
        default_version='v1',
        description="Issuing Receciving APIs"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(BearerAuthentication,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('election/', include('election.urls')),
    path(r'report-to-work/', include("part_one.urls")),
    path(r'staffs/', include("staffs.urls")),
    path("units/", include("units.urls")),
    path("part-two/", include("part_two.urls")),
    path("part-three/", include("part_three.urls")),
    path("part-four/", include("part_four.urls")),
    path("part-five/", include("part_five.urls")),
    path("auth/", views.obtain_auth_token),
    url(r'^$', schema_view.with_ui('swagger',
                                   cache_timeout=0), name='schema-swagger-ui')
]
