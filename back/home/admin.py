from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Cover, Nominee, Stage, Jury, AwardCeremony, \
    Partner, Document, FAQ


@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.all().exists() is False


@admin.register(Nominee)
class NomineeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = (
        'nomination',
        'project_name',
        'founder',
        'is_winner',
    )
    list_filter = (
        'nomination',
        'is_winner',
    )


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = (
        'stage',
        'start_date',
        'stop_date',
    )


@admin.register(Jury)
class JuryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(AwardCeremony)
class AwardCeremonyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.all().exists() is False


@admin.register(Partner)
class PartnerAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return self.model.objects.all().count() < len(self.model.NAME_CHOICES)

@admin.register(FAQ)
class FAQAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
