from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event, Siteuser, Car
from django import forms


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_date')
    template_name = 'index.html'
    paginate_by = 10


class EventView(View):
    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        is_attendee = False
        if event.attendee.filter(id=self.request.user.id).exists():
            is_attendee = True

        return render(request, 'eventview.html', {'event': event, 'is_attendee': is_attendee, })

    def post(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        is_attendee = False
        if event.attendee.filter(id=self.request.user.id).exists():
            is_attendee = True

        return render(request, 'eventview.html', {'event': event, 'is_attendee': is_attendee, })


class EventReg(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventreg.html', {'event': event})


class EventUnReg(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventunreg.html', {'event': event})


class YourEventList(generic.ListView):
    model = Event
    template_name = 'yourevents.html'
    paginate_by = 10

    def get_queryset(self):
        your_event_list = Event.objects.filter(attendee=self.request.user)
        return your_event_list


class EventOrg(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_date')
    template_name = 'eventorg.html'
    paginate_by = 10


def OwnConPan(request):
    return render(request, 'ownconpan.html', {})


class UserReg(View):
    def post(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        if event.attendee.filter(id=request.user.id).exists():
            event.attendee.remove(request.user)
            return render(request, 'eventreg.html', {})
        else:
            event.attendee.add(request.user)
            return render(request, 'eventreg.html', {})
