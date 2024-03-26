"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from apply.views import FirstStepViewSet, CallMeViewSet, \
    AgroMachineryViewSet, AgroDigitalViewSet, FutureFoodViewSet, \
    MadeInRussiaViewSet, AgroHeroViewSet, AgroLaunchViewSet, AgroIdeaViewSet, test_email
from home.views import home, apply_form

router = DefaultRouter()
router.register(r'call_me', CallMeViewSet)
router.register(r'first_step', FirstStepViewSet)
router.register(r'agro_machinery', AgroMachineryViewSet)
router.register(r'agro_digital', AgroDigitalViewSet)
router.register(r'future_food', FutureFoodViewSet)
router.register(r'made_in_russia', MadeInRussiaViewSet)
router.register(r'agro_hero', AgroHeroViewSet)
router.register(r'agro_launch', AgroLaunchViewSet)
router.register(r'agro_idea', AgroIdeaViewSet)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home, name="home"),
    path('apply', apply_form, name="apply_form"),
    path('test_email/', test_email),
    path('tinymce/', include('tinymce.urls')),
]
