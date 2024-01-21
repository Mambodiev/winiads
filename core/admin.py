from django.contrib import admin
from . import models
from core.models import Faq, Setting, Privacy, Term



class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'ordernumber', 'status']
    list_filter = ['status']

    
class SettingAdmin(admin.ModelAdmin):
    list_display = ['header_one', 'create_at', 'update_at']


class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['header', 'create_at', 'update_at']
    

class TermAdmin(admin.ModelAdmin):
    list_display = ['header', 'create_at', 'update_at']

admin.site.register(Faq,FaqAdmin)
admin.site.register(Setting,SettingAdmin)
admin.site.register(Privacy,PrivacyAdmin)
admin.site.register(Term,TermAdmin)
