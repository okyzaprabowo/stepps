from django.contrib import admin
from dashboard.models import * 

# Register your models here.
class SteppsResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at')
    fields = ['keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', ]

admin.site.register(SteppsResult, SteppsResultAdmin)