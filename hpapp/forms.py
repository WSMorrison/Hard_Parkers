from .models import Event
from django import forms


class EventForm(forms.ModelForm):
    event_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'date'}))
    event_date_reg_close = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_date_reg_close',
                  'event_location', 'event_location_url',
                  'number_cars', 'event_description',)


class EditForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_date_reg_close',
                  'event_location', 'event_location_url',
                  'number_cars', 'event_description',)
