from django.contrib import admin
from dashboard.models import * 

# Register your models here.
class SteppsResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', 'created_at')
    fields = ['keyword', 'freq_high', 'px_high', 'freq_medium', 'px_medium', 'freq_low', 'px_low', 'label', ]

class ClassificationResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'label', 'created_at')
    fields = ['keyword', 'label', ]

class CrawlingAdmin(admin.ModelAdmin):
    list_display = ('username', 'follower_count', 'taken_at', 'like_count', 'caption_text', 'time_frame', 'engagement', 'created_at')
    fields = ['username', 'follower_count', 'taken_at', 'like_count', 'caption_text', 'time_frame', 'engagement', ]

admin.site.register(SteppsResult, SteppsResultAdmin)
admin.site.register(ClassificationResult, ClassificationResultAdmin)
admin.site.register(Crawling, CrawlingAdmin)