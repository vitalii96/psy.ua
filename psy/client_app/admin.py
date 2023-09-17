from django.contrib import admin

from .models import *

from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    # Перелік полів, які будуть відображатись у формі створення/редагування
    fields = ('user', 'contact_number', 'issue_description', 'first_name', 'last_name')

    # Перелік полів, які будуть відображатись у списку клієнтів у адмін панелі
    list_display = ('user', 'contact_number', 'first_name', 'last_name', 'created_at')


admin.site.register(Client, ClientAdmin)


class SessionRecordAdmin(admin.ModelAdmin):
    fields = ('client', 'session_date', 'session_time', 'status')
    list_display = ('client', 'session_date', 'session_time', 'status')
    list_editable = ('status','session_time', 'session_date')
    search_fields = ('status', 'client__first_name', 'client__last_name','session_time')
    list_filter = ('status', 'client','session_date')


admin.site.register(SessionRecord, SessionRecordAdmin)
