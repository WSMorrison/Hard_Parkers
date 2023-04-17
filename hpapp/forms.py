from .models import Event
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Field, MultiField, Div, Fieldset
from crispy_forms.bootstrap import InlineField
from datetime import datetime


# Custom validators.
def google_maps_ok(value):
    if value.startswith('https://goo.gl/maps/') is False:
        raise forms.ValidationError('On Google Maps copy and paste from SHARE')


def number_cars_ok(value):
    if value <= 0:
        raise forms.ValidationError("There can't be any parking without cars!")
    elif value > 199:
        raise forms.ValidationError("Maximum is 199 at this time.")


# Form for Event creation and Event editing
class EventForm(forms.ModelForm):
    event_date = forms.DateTimeField(label='The event date:',
                                     widget=forms.TextInput(attrs={
                                       'type': 'date', 'min':
                                       datetime.now().date()
                                       }))
    event_date_reg_close = forms.DateTimeField(label='Registration closes:',
                                               widget=forms.TextInput(attrs={
                                                 'type': 'date',
                                                 'min': datetime.now().date(),
                                                 'max': event_date
                                                 }))

    event_location_url = forms.CharField(label='Share Google Maps link here:',
                                         validators=[google_maps_ok],
                                         widget=forms.URLInput(attrs={
                                          'placeholder': 'https://goo.gl/maps/'
                                          }))

    number_cars = forms.IntegerField(label='How many cars may register?',
                                     validators=[number_cars_ok],
                                     widget=forms.TextInput(attrs={
                                      'placeholder': 'Max 199'
                                      }))

    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_time',
                  'event_date_reg_close', 'event_time_reg_close',
                  'event_location', 'event_location_url',
                  'number_cars', 'event_description',)
        labels = {'event_name': 'Your event name:',
                  'event_date': 'The event date:',
                  'event_time': 'At time:',
                  'event_time_reg_close': 'At time:',
                  'event_location': 'The location:',
                  'number_cars': 'How many cars can you accomodate?',
                  'event_description': 'Briefly describe your event:'}
