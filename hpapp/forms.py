from .models import Event
from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Field, MultiField, Div, Fieldset
from crispy_forms.bootstrap import InlineField
from datetime import datetime


# Form for Event creation.
class EventForm(forms.ModelForm):
    event_date = forms.DateTimeField(label='The event date:',
                                     widget=forms.TextInput(attrs={
                                       'type': 'date', 'min':
                                       datetime.now().date()}
                                       ))
    event_date_reg_close = forms.DateTimeField(label='Registration closes:',
                                               widget=forms.TextInput(attrs={
                                                 'type': 'date',
                                                 'min': datetime.now().date()}
                                                 ))

    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_time',
                  'event_date_reg_close', 'event_time_reg_close',
                  'event_location',
                  'number_cars', 'event_description',)
        labels = {'event_name': 'Your event name:',
                  'event_date': 'The event date:',
                  'event_time': 'At time:',
                  'event_time_reg_close': 'At time:',
                  'event_location': 'The location:',
                  'number_cars': 'How many cars can you accomodate?',
                  'event_description': 'Briefly describe your event:'}
