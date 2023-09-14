from django.contrib import admin
from . import models
from core.models import Faq



class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'ordernumber', 'status']
    list_filter = ['status']

admin.site.register(Faq,FaqAdmin)
