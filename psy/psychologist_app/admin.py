from django.contrib import admin

from .models import *


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'image')
    list_editable = ('image',)


class PsychoLogistAdmin(admin.ModelAdmin):
    list_display = ('user',)


class SignAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ContentItemsAdmin(admin.ModelAdmin):
    list_display = ('title','sign')


admin.site.register(Diploma)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Psychologist, PsychoLogistAdmin)
admin.site.register(ContentItems,ContentItemsAdmin )
admin.site.register(Sign,SignAdmin)

admin.site.site_title = 'Адмін-панель'
admin.site.site_header = 'Адмін-панель'
