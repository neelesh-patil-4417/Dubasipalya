from django.contrib import admin
from base.models import schedule
# Register your models here.


from base.resources import schedule_resources
from import_export.admin import ImportExportModelAdmin

@admin.register(schedule)
class yourmodeladmin(ImportExportModelAdmin):
    resource_class = schedule_resources
