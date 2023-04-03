from django.contrib import admin
from .models import Event, Siteuser


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    title = ('Event Date')
    list_filter = ('event_date', 'organizer', 'attendee',)


@admin.register(Siteuser)
class SiteuserAdmin(admin.ModelAdmin):
    list_filter = ('event_organizer',)
