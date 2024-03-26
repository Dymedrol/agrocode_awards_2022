from rest_framework import serializers

from .models import FirstStep, CallMe, AgroMachinery, AgroDigital, \
    FutureFood, MadeInRussia, AgroHero, AgroLaunch, AgroIdea


class CallMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallMe
        fields = (
            'telegram',
            'email',
            'agree_processing',
        )


class FirstStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstStep
        exclude = ('dt',)


class AgroMachinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroMachinery
        exclude = ('dt', 'nomination')


class AgroDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroDigital
        exclude = ('dt', 'nomination')


class FutureFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutureFood
        exclude = ('dt', 'nomination')


class MadeInRussiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MadeInRussia
        exclude = ('dt', 'nomination')


class AgroHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroHero
        exclude = ('dt', 'nomination')


class AgroLaunchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroLaunch
        exclude = ('dt', 'nomination')


class AgroIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroIdea
        exclude = ('dt', 'nomination')
