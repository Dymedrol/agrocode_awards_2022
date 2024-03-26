from django.shortcuts import render
from rest_framework import viewsets

from core.utils import send_rich_mail
from .models import FirstStep, CallMe, AgroMachinery, AgroDigital, \
    FutureFood, MadeInRussia, AgroHero, AgroLaunch, AgroIdea
from .serializers import FirstStepSerializer, CallMeSerializer, \
    AgroMachinerySerializer, AgroDigitalSerializer, FutureFoodSerializer, \
    MadeInRussiaSerializer, AgroHeroSerializer, AgroLaunchSerializer, \
    AgroIdeaSerializer


class CallMeViewSet(viewsets.ModelViewSet):
    serializer_class = CallMeSerializer
    queryset = CallMe.objects.none()


class ApplySendEmailMixing(object):
    def perform_create(self, serializer):
        instance = serializer.save()

        email_data = {
            'subject': 'Спасибо за заявку!',
            'email_to': [instance.email, ],
            'email_from': '"Команда AgroCode" <hello@agro-code.ru>',
            'template': 'apply/emails/thx_email.html',
            'data': {
                'instance': instance,
            },
        }
        send_rich_mail(**email_data)


class FirstStepViewSet(viewsets.ModelViewSet):
    serializer_class = FirstStepSerializer
    queryset = FirstStep.objects.none()


class AgroMachineryViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = AgroMachinerySerializer
    queryset = AgroMachinery.objects.none()


class AgroDigitalViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = AgroDigitalSerializer
    queryset = AgroDigital.objects.none()


class FutureFoodViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = FutureFoodSerializer
    queryset = FutureFood.objects.none()


class MadeInRussiaViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = MadeInRussiaSerializer
    queryset = MadeInRussia.objects.none()


class AgroHeroViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = AgroHeroSerializer
    queryset = AgroHero.objects.none()


class AgroLaunchViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = AgroLaunchSerializer
    queryset = AgroLaunch.objects.none()


class AgroIdeaViewSet(ApplySendEmailMixing, viewsets.ModelViewSet):
    serializer_class = AgroIdeaSerializer
    queryset = AgroIdea.objects.none()

def test_email(request):
    return render(request, 'apply/emails/thx_email.html', {})
