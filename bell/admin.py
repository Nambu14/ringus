from django.contrib import admin

from .models import Account, Visitor, Notification, Message, Visit

# Register your models here.
admin.site.register(Visitor)
admin.site.register(Notification)
admin.site.register(Visit)
