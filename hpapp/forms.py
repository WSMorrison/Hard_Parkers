from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_date_reg_close',
                  'event_location', 'event_location_url',
                  'number_cars', 'event_description',)
