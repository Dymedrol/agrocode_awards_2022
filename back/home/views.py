import datetime

from django.conf import settings
from django.shortcuts import render, redirect

from .models import Cover, Nominee, Stage, Jury, AwardCeremony, Partner, \
    Document, STAGE_CHOICES, FAQ


def home(request):
    stages_dict = dict()
    current_stage = None
    today = datetime.date.today()
    for s in STAGE_CHOICES:
        stage_draft = Stage.objects.filter(stage=s[0]).first()
        if not stage_draft:
            continue
        if not current_stage and stage_draft.stop_date >= today:
            current_stage = stage_draft.get_stage_display()
            stage_draft.is_active = True
        stages_dict[s[0]] = stage_draft

    data = {
        'is_stop_date': datetime.datetime.now() >= settings.APPLY_STOP_DT,
        'cover': Cover.objects.first() or Cover(),
        'nominees': Nominee.objects.all(),
        'nominees_machinery': Nominee.objects.filter(nomination='agro_machinery'),
        'nominees_digital': Nominee.objects.filter(nomination='agro_digital'),
        'nominees_food': Nominee.objects.filter(nomination='future_food'),
        'nominees_russia': Nominee.objects.filter(nomination='made_in_russia'),
        'nominees_hero': Nominee.objects.filter(nomination='agro_hero'),
        'nominees_launch': Nominee.objects.filter(nomination='agro_launch'),
        'nominees_idea': Nominee.objects.filter(nomination='agro_idea'),
        'winners': Nominee.objects.filter(is_winner=True),
        'stages': stages_dict,
        'current_stage': current_stage,
        'juries': Jury.objects.all(),
        'award_ceremony': AwardCeremony.objects.first(),
        'partners': Partner.objects.all(),
        'documents': {d.name: d.file for d in Document.objects.all()},
        'faqs': FAQ.objects.all(),
    }
    return render(request, 'home.html', data)


def apply_form(request):
    if datetime.datetime.now() >= settings.APPLY_STOP_DT:
        return redirect('/')

    data = {
        'cover': Cover.objects.first() or Cover(),
        'juries': Jury.objects.all(),
        'documents': {d.name: d.file for d in Document.objects.all()},
        'is_form': 'true',
    }
    return render(request, 'form.html', data)
