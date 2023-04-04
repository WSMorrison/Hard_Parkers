from .models import Event
from django import forms
from crispy_forms.helper import FormHelper
from datetime import datetime


class EventForm(forms.ModelForm):
    event_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'date', 'min': datetime.now().date()}))
    event_date_reg_close = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'date', 'min': datetime.now().date()}))

    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_time',
                  'event_date_reg_close', 'event_time_reg_close',
                  'event_location', 'event_location_url',
                  'number_cars', 'event_description',)


class EditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_date_reg_close',
                  'event_location', 'event_location_url',
                  'number_cars', 'event_description',)
