from django.contrib import admin
from analytical.models import ViewModel, AnalyticMedia
from unfold.contrib.import_export.forms import ExportForm
from unfold.admin import ModelAdmin
from import_export.admin import ExportActionModelAdmin


admin.site.register(AnalyticMedia, ModelAdmin)


@admin.register(ViewModel)
class ViewModelAdmin(ModelAdmin, ExportActionModelAdmin):
    export_form_class = ExportForm
    ...
