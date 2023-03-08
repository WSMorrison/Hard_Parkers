from django.contrib import admin
from .models import Event, Car, Siteuser


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    title = ('Event Date')
    list_filter = ('event_date',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ('car_year',)


@admin.register(Siteuser)
class SiteuserAdmin(admin.ModelAdmin):
    list_filter = ('event_organizer',)
