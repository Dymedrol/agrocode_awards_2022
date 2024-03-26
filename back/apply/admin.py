from io import BytesIO
import xlwt
import re


from django.contrib import admin
from django.http import HttpResponse

from .models import FirstStep, CallMe, AgroMachinery, AgroDigital, \
    FutureFood, MadeInRussia, AgroHero, AgroLaunch, AgroIdea


@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'telegram',
        'dt',
    )
    search_fields = (
        'email',
        'telegram',
    )
    list_filter = (
        'dt',
    )

    actions = ('make_export', 'make_export_excel_select',)

    def make_export(modeladmin, request, queryset):
        FIELDS_PROJECT = []
        col = 0
        for f in CallMe._meta.fields:
            if not f.name == u'id':
                FIELDS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Invoice')

        for f in FIELDS_PROJECT:
            ws.write(1, f[0], f[2])

        offset = 1
        for o in CallMe.objects.all():
            offset += 1
            for f in FIELDS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"

    def make_export_excel_select(modeladmin, request, queryset):
        FIELDS_PROJECT = []
        col = 0
        for f in CallMe._meta.fields:
            if not f.name == u'id':
                FIELDS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Invoice')

        for f in FIELDS_PROJECT:
            ws.write(1, f[0], f[2])

        offset = 1
        for o in queryset:
            offset += 1
            for f in FIELDS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export_excel_select.short_description = u"Экспорт выбранных записей в Excel"


@admin.register(FirstStep)
class FirstStepAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'dt',)

    actions = ('make_export', 'make_export_excel_select',)

    def make_export(modeladmin, request, queryset):
        FIELDS_PROJECT = []
        col = 0
        for f in FirstStep._meta.fields:
            if not f.name == u'id':
                FIELDS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Invoice')

        for f in FIELDS_PROJECT:
            ws.write(1, f[0], f[2])

        offset = 1
        for o in FirstStep.objects.all():
            offset += 1
            for f in FIELDS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"

    def make_export_excel_select(modeladmin, request, queryset):
        FIELDS_PROJECT = []
        col = 0
        for f in FirstStep._meta.fields:
            if not f.name == u'id':
                FIELDS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Invoice')

        for f in FIELDS_PROJECT:
            ws.write(1, f[0], f[2])

        offset = 1
        for o in queryset:
            offset += 1
            for f in FIELDS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export_excel_select.short_description = u"Экспорт выбранных записей в Excel"


class ApplyAdminBase(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'email',
        'dt',
    )
    search_fields = (
        'name',
        'surname',
        'email',
    )
    list_filter = (
        'dt',
    )


def get_links(chat_string):
    pattern = '(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?'
    return re.findall(pattern, chat_string)


style = xlwt.XFStyle()
style.alignment.wrap = 1


@admin.register(FutureFood)
class FutureFoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dt',)
    search_fields = ('name', 'surname', 'email',)
    list_filter = ('dt',)

    actions = ('make_export', )

    def make_export(modeladmin, request, queryset):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Еда будущего')
        ws2 = wb.add_sheet('Запуск года')
        ws3 = wb.add_sheet('Идея года')
        ws4 = wb.add_sheet('Лидер года')
        ws5 = wb.add_sheet('Своя технология')
        ws6 = wb.add_sheet('Цифровизация года')

        FOODS_PROJECT = []
        col = 0
        for f in FutureFood._meta.fields:
            if not f.name == u'id':
                FOODS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in FOODS_PROJECT:
            ws.write(0, f[0], f[2])

        offset = 0
        for o in FutureFood.objects.all():
            offset += 1
            for f in FOODS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        LAUNCH_PROJECT = []
        col = 0
        for f in AgroLaunch._meta.fields:
            if not f.name == u'id':
                LAUNCH_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in LAUNCH_PROJECT:
            ws2.write(0, f[0], f[2])

        offset = 0
        for o in AgroLaunch.objects.all():
            offset += 1
            for f in LAUNCH_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws2.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws2.write(offset, f[0], str(val))

        IDEA_PROJECT = []
        col = 0
        for f in AgroIdea._meta.fields:
            if not f.name == u'id':
                IDEA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in IDEA_PROJECT:
            ws3.write(0, f[0], f[2])

        offset = 0
        for o in AgroIdea.objects.all():
            offset += 1
            for f in IDEA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws3.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == 16:
                        ws3.write(offset, f[0], str(val), style)
                    else:
                        ws3.write(offset, f[0], str(val))


        HERO_PROJECT = []
        col = 0
        for f in AgroHero._meta.fields:
            if not f.name == u'id':
                HERO_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in HERO_PROJECT:
            ws4.write(0, f[0], f[2])

        offset = 0
        for o in AgroHero.objects.all():
            offset += 1
            list_len = len(HERO_PROJECT) - 1
            for f in HERO_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws4.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == list_len:
                        ws4.write(offset, f[0], str(val), style)
                    else:
                        ws4.write(offset, f[0], str(val))

        RUSSIA_PROJECT = []
        col = 0
        for f in MadeInRussia._meta.fields:
            if not f.name == u'id':
                RUSSIA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in RUSSIA_PROJECT:
            ws5.write(0, f[0], f[2])

        offset = 0
        for o in MadeInRussia.objects.all():
            offset += 1
            for f in RUSSIA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws5.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws5.write(offset, f[0], str(val))

        DIGITAL_PROJECT = []
        col = 0
        for f in AgroDigital._meta.fields:
            if not f.name == u'id':
                DIGITAL_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in DIGITAL_PROJECT:
            ws6.write(0, f[0], f[2])

        offset = 0
        for o in AgroDigital.objects.all():
            offset += 1
            for f in DIGITAL_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws6.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws6.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"


@admin.register(AgroDigital)
class AgroDigitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dt',)
    search_fields = ('name', 'surname', 'email',)
    list_filter = ('dt',)

    actions = ('make_export', )

    def make_export(modeladmin, request, queryset):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Еда будущего')
        ws2 = wb.add_sheet('Запуск года')
        ws3 = wb.add_sheet('Идея года')
        ws4 = wb.add_sheet('Лидер года')
        ws5 = wb.add_sheet('Своя технология')
        ws6 = wb.add_sheet('Цифровизация года')

        FOODS_PROJECT = []
        col = 0
        for f in FutureFood._meta.fields:
            if not f.name == u'id':
                FOODS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in FOODS_PROJECT:
            ws.write(0, f[0], f[2])

        offset = 0
        for o in FutureFood.objects.all():
            offset += 1
            for f in FOODS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        LAUNCH_PROJECT = []
        col = 0
        for f in AgroLaunch._meta.fields:
            if not f.name == u'id':
                LAUNCH_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in LAUNCH_PROJECT:
            ws2.write(0, f[0], f[2])

        offset = 0
        for o in AgroLaunch.objects.all():
            offset += 1
            for f in LAUNCH_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws2.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws2.write(offset, f[0], str(val))

        IDEA_PROJECT = []
        col = 0
        for f in AgroIdea._meta.fields:
            if not f.name == u'id':
                IDEA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in IDEA_PROJECT:
            ws3.write(0, f[0], f[2])

        offset = 0
        for o in AgroIdea.objects.all():
            offset += 1
            for f in IDEA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws3.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == 16:
                        ws3.write(offset, f[0], str(val), style)
                    else:
                        ws3.write(offset, f[0], str(val))


        HERO_PROJECT = []

        col = 0
        for f in AgroHero._meta.fields:
            if not f.name == u'id':
                HERO_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in HERO_PROJECT:
            ws4.write(0, f[0], f[2])

        offset = 0
        for o in AgroHero.objects.all():
            offset += 1
            list_len = len(HERO_PROJECT) - 1
            for f in HERO_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws4.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == list_len:
                        ws4.write(offset, f[0], str(val), style)
                    else:
                        ws4.write(offset, f[0], str(val))

        RUSSIA_PROJECT = []
        col = 0
        for f in MadeInRussia._meta.fields:
            if not f.name == u'id':
                RUSSIA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in RUSSIA_PROJECT:
            ws5.write(0, f[0], f[2])

        offset = 0
        for o in MadeInRussia.objects.all():
            offset += 1
            for f in RUSSIA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws5.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws5.write(offset, f[0], str(val))

        DIGITAL_PROJECT = []
        col = 0
        for f in AgroDigital._meta.fields:
            if not f.name == u'id':
                DIGITAL_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in DIGITAL_PROJECT:
            ws6.write(0, f[0], f[2])

        offset = 0
        for o in AgroDigital.objects.all():
            offset += 1
            for f in DIGITAL_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws6.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws6.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"


@admin.register(MadeInRussia)
class MadeInRussiaAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dt',)
    search_fields = ('name', 'surname', 'email',)
    list_filter = ('dt',)

    actions = ('make_export', )

    def make_export(modeladmin, request, queryset):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Еда будущего')
        ws2 = wb.add_sheet('Запуск года')
        ws3 = wb.add_sheet('Идея года')
        ws4 = wb.add_sheet('Лидер года')
        ws5 = wb.add_sheet('Своя технология')
        ws6 = wb.add_sheet('Цифровизация года')

        FOODS_PROJECT = []
        col = 0
        for f in FutureFood._meta.fields:
            if not f.name == u'id':
                FOODS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in FOODS_PROJECT:
            ws.write(0, f[0], f[2])

        offset = 0
        for o in FutureFood.objects.all():
            offset += 1
            for f in FOODS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        LAUNCH_PROJECT = []
        col = 0
        for f in AgroLaunch._meta.fields:
            if not f.name == u'id':
                LAUNCH_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in LAUNCH_PROJECT:
            ws2.write(0, f[0], f[2])

        offset = 0
        for o in AgroLaunch.objects.all():
            offset += 1
            for f in LAUNCH_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws2.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws2.write(offset, f[0], str(val))

        IDEA_PROJECT = []
        col = 0
        for f in AgroIdea._meta.fields:
            if not f.name == u'id':
                IDEA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in IDEA_PROJECT:
            ws3.write(0, f[0], f[2])

        offset = 0
        for o in AgroIdea.objects.all():
            offset += 1
            for f in IDEA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws3.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == 16:
                        ws3.write(offset, f[0], str(val), style)
                    else:
                        ws3.write(offset, f[0], str(val))


        HERO_PROJECT = []

        col = 0
        for f in AgroHero._meta.fields:
            if not f.name == u'id':
                HERO_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in HERO_PROJECT:
            ws4.write(0, f[0], f[2])

        offset = 0
        for o in AgroHero.objects.all():
            offset += 1
            list_len = len(HERO_PROJECT) - 1
            for f in HERO_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws4.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == list_len:
                        ws4.write(offset, f[0], str(val), style)
                    else:
                        ws4.write(offset, f[0], str(val))

        RUSSIA_PROJECT = []
        col = 0
        for f in MadeInRussia._meta.fields:
            if not f.name == u'id':
                RUSSIA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in RUSSIA_PROJECT:
            ws5.write(0, f[0], f[2])

        offset = 0
        for o in MadeInRussia.objects.all():
            offset += 1
            for f in RUSSIA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws5.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws5.write(offset, f[0], str(val))

        DIGITAL_PROJECT = []
        col = 0
        for f in AgroDigital._meta.fields:
            if not f.name == u'id':
                DIGITAL_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in DIGITAL_PROJECT:
            ws6.write(0, f[0], f[2])

        offset = 0
        for o in AgroDigital.objects.all():
            offset += 1
            for f in DIGITAL_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws6.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws6.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"


@admin.register(AgroIdea)
class AgroIdeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dt',)
    search_fields = ('name', 'surname', 'email',)
    list_filter = ('dt',)

    actions = ('make_export', )

    def make_export(modeladmin, request, queryset):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Еда будущего')
        ws2 = wb.add_sheet('Запуск года')
        ws3 = wb.add_sheet('Идея года')
        ws4 = wb.add_sheet('Лидер года')
        ws5 = wb.add_sheet('Своя технология')
        ws6 = wb.add_sheet('Цифровизация года')

        FOODS_PROJECT = []
        col = 0
        for f in FutureFood._meta.fields:
            if not f.name == u'id':
                FOODS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in FOODS_PROJECT:
            ws.write(0, f[0], f[2])

        offset = 0
        for o in FutureFood.objects.all():
            offset += 1
            for f in FOODS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        LAUNCH_PROJECT = []
        col = 0
        for f in AgroLaunch._meta.fields:
            if not f.name == u'id':
                LAUNCH_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in LAUNCH_PROJECT:
            ws2.write(0, f[0], f[2])

        offset = 0
        for o in AgroLaunch.objects.all():
            offset += 1
            for f in LAUNCH_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws2.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws2.write(offset, f[0], str(val))

        IDEA_PROJECT = []
        col = 0
        for f in AgroIdea._meta.fields:
            if not f.name == u'id':
                IDEA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in IDEA_PROJECT:
            ws3.write(0, f[0], f[2])

        offset = 0
        for o in AgroIdea.objects.all():
            offset += 1
            for f in IDEA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws3.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == 16:
                        ws3.write(offset, f[0], str(val), style)
                    else:
                        if f[0] == 16:
                            ws3.write(offset, f[0], str(val), style)
                        else:
                            ws3.write(offset, f[0], str(val))


        HERO_PROJECT = []

        col = 0
        for f in AgroHero._meta.fields:
            if not f.name == u'id':
                HERO_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in HERO_PROJECT:
            ws4.write(0, f[0], f[2])

        offset = 0
        for o in AgroHero.objects.all():
            offset += 1
            list_len = len(HERO_PROJECT) - 1
            for f in HERO_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws4.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == list_len:
                        ws4.write(offset, f[0], str(val), style)
                    else:
                        ws4.write(offset, f[0], str(val))

        RUSSIA_PROJECT = []
        col = 0
        for f in MadeInRussia._meta.fields:
            if not f.name == u'id':
                RUSSIA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in RUSSIA_PROJECT:
            ws5.write(0, f[0], f[2])

        offset = 0
        for o in MadeInRussia.objects.all():
            offset += 1
            for f in RUSSIA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws5.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws5.write(offset, f[0], str(val))

        DIGITAL_PROJECT = []
        col = 0
        for f in AgroDigital._meta.fields:
            if not f.name == u'id':
                DIGITAL_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in DIGITAL_PROJECT:
            ws6.write(0, f[0], f[2])

        offset = 0
        for o in AgroDigital.objects.all():
            offset += 1
            for f in DIGITAL_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws6.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws6.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"


@admin.register(AgroHero)
class AgroHeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dt',)
    search_fields = ('name', 'surname', 'email',)
    list_filter = ('dt',)

    actions = ('make_export', )

    def make_export(modeladmin, request, queryset):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Еда будущего')
        ws2 = wb.add_sheet('Запуск года')
        ws3 = wb.add_sheet('Идея года')
        ws4 = wb.add_sheet('Лидер года')
        ws5 = wb.add_sheet('Своя технология')
        ws6 = wb.add_sheet('Цифровизация года')

        FOODS_PROJECT = []
        col = 0
        for f in FutureFood._meta.fields:
            if not f.name == u'id':
                FOODS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in FOODS_PROJECT:
            ws.write(0, f[0], f[2])

        offset = 0
        for o in FutureFood.objects.all():
            offset += 1
            for f in FOODS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        LAUNCH_PROJECT = []
        col = 0
        for f in AgroLaunch._meta.fields:
            if not f.name == u'id':
                LAUNCH_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in LAUNCH_PROJECT:
            ws2.write(0, f[0], f[2])

        offset = 0
        for o in AgroLaunch.objects.all():
            offset += 1
            for f in LAUNCH_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws2.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws2.write(offset, f[0], str(val))

        IDEA_PROJECT = []
        col = 0
        for f in AgroIdea._meta.fields:
            if not f.name == u'id':
                IDEA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in IDEA_PROJECT:
            ws3.write(0, f[0], f[2])

        offset = 0
        for o in AgroIdea.objects.all():
            offset += 1
            for f in IDEA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws3.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == 16:
                        ws3.write(offset, f[0], str(val), style)
                    else:
                        ws3.write(offset, f[0], str(val))


        HERO_PROJECT = []
        col = 0
        for f in AgroHero._meta.fields:
            if not f.name == u'id':
                HERO_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in HERO_PROJECT:
            ws4.write(0, f[0], f[2])

        offset = 0
        for o in AgroHero.objects.all():
            offset += 1
            list_len = len(HERO_PROJECT) - 1
            for f in HERO_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws4.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == list_len:
                        ws4.write(offset, f[0], str(val), style)
                    else:
                        ws4.write(offset, f[0], str(val))

        RUSSIA_PROJECT = []
        col = 0
        for f in MadeInRussia._meta.fields:
            if not f.name == u'id':
                RUSSIA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in RUSSIA_PROJECT:
            ws5.write(0, f[0], f[2])

        offset = 0
        for o in MadeInRussia.objects.all():
            offset += 1
            for f in RUSSIA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws5.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws5.write(offset, f[0], str(val))

        DIGITAL_PROJECT = []
        col = 0
        for f in AgroDigital._meta.fields:
            if not f.name == u'id':
                DIGITAL_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in DIGITAL_PROJECT:
            ws6.write(0, f[0], f[2])

        offset = 0
        for o in AgroDigital.objects.all():
            offset += 1
            for f in DIGITAL_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws6.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws6.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"


@admin.register(AgroLaunch)
class AgroLaunchAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'dt',)
    search_fields = ('name', 'surname', 'email',)
    list_filter = ('dt',)

    actions = ('make_export', )

    def make_export(modeladmin, request, queryset):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Еда будущего')
        ws2 = wb.add_sheet('Запуск года')
        ws3 = wb.add_sheet('Идея года')
        ws4 = wb.add_sheet('Лидер года')
        ws5 = wb.add_sheet('Своя технология')
        ws6 = wb.add_sheet('Цифровизация года')

        FOODS_PROJECT = []
        col = 0
        for f in FutureFood._meta.fields:
            if not f.name == u'id':
                FOODS_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in FOODS_PROJECT:
            ws.write(0, f[0], f[2])

        offset = 0
        for o in FutureFood.objects.all():
            offset += 1
            for f in FOODS_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws.write(offset, f[0], str(val))

        LAUNCH_PROJECT = []
        col = 0
        for f in AgroLaunch._meta.fields:
            if not f.name == u'id':
                LAUNCH_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in LAUNCH_PROJECT:
            ws2.write(0, f[0], f[2])

        offset = 0
        for o in AgroLaunch.objects.all():
            offset += 1
            for f in LAUNCH_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws2.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws2.write(offset, f[0], str(val))

        IDEA_PROJECT = []
        col = 0
        for f in AgroIdea._meta.fields:
            if not f.name == u'id':
                IDEA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in IDEA_PROJECT:
            ws3.write(0, f[0], f[2])

        offset = 0
        for o in AgroIdea.objects.all():
            offset += 1
            for f in IDEA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws3.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == 16:
                        ws3.write(offset, f[0], str(val), style)
                    else:
                        if f[0] == 16:
                            ws3.write(offset, f[0], str(val), style)
                        else:
                            ws3.write(offset, f[0], str(val))


        HERO_PROJECT = []
        col = 0
        for f in AgroHero._meta.fields:
            if not f.name == u'id':
                HERO_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in HERO_PROJECT:
            ws4.write(0, f[0], f[2])

        offset = 0
        for o in AgroHero.objects.all():
            offset += 1
            list_len = len(HERO_PROJECT) - 1
            for f in HERO_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws4.write(offset, f[0], getattr(o, get_display)())
                else:
                    if f[0] == list_len:
                        ws4.write(offset, f[0], str(val), style)
                    else:
                        ws4.write(offset, f[0], str(val))

        RUSSIA_PROJECT = []
        col = 0
        for f in MadeInRussia._meta.fields:
            if not f.name == u'id':
                RUSSIA_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in RUSSIA_PROJECT:
            ws5.write(0, f[0], f[2])

        offset = 0
        for o in MadeInRussia.objects.all():
            offset += 1
            for f in RUSSIA_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws5.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws5.write(offset, f[0], str(val))

        DIGITAL_PROJECT = []
        col = 0
        for f in AgroDigital._meta.fields:
            if not f.name == u'id':
                DIGITAL_PROJECT.append((col, f.name, f.verbose_name))
                col += 1

        for f in DIGITAL_PROJECT:
            ws6.write(0, f[0], f[2])

        offset = 0
        for o in AgroDigital.objects.all():
            offset += 1
            for f in DIGITAL_PROJECT:
                val = getattr(o, f[1], None)
                if not val:
                    continue
                get_display = u'get_%s_display' % f[1]
                if hasattr(o, get_display):
                    ws6.write(offset, f[0], getattr(o, get_display)())
                else:
                    ws6.write(offset, f[0], str(val))

        tmpfile = BytesIO()
        wb.save(tmpfile)
        tmpfile.seek(0)
        response = HttpResponse(
            tmpfile.read(), content_type='application/octet-stream'
        )
        response[
            'Content-Disposition'
        ] = 'attachment; filename="application_export.xls"'
        return response

    make_export.short_description = u"Экспорт ВСЕХ записей"
