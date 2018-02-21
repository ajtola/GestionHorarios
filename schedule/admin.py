from django.contrib import admin
from schedule.models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('start', 'finish', 'hours_worked', 'worker')

# Register your models here.
admin.site.register(Schedule, ScheduleAdmin)