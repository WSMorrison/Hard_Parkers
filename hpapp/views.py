from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event, Siteuser, Car
from .forms import EventForm
from django import forms


# Good
# Home page.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by('event_date')
    template_name = 'index.html'
    paginate_by = 10


# Good
# Logged in user's list of events they have already registered for.
class YourEventList(generic.ListView):
    model = Event
    template_name = 'yourevents.html'
    paginate_by = 10

    def get_queryset(self):
        your_event_list = Event.objects.filter(attendee=self.request.user
                                               ).order_by('event_date')
        return your_event_list


# Good
# Event organizer's list of events they have organized.
class EventOrg(generic.ListView):
    model = Event
    template_name = 'eventorg.html'
    paginate_by = 10

    def get_queryset(self):
        your_event_list = Event.objects.filter(organizer=self.request.user)
        return your_event_list


# Placeholder
# Owner control panel for approving event organizers, etc.
def OwnConPan(request):
    return render(request, 'ownconpan.html', {})


# Good
# Logged in user can view an event and either register for it if not
# already registered, and unregister if already registered.
class EventView(View):
    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        is_attendee = False
        if event.attendee.filter(id=self.request.user.id).exists():
            is_attendee = True

        return render(request, 'eventview.html',
                      {'event': event, 'is_attendee': is_attendee, })

    def post(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        is_attendee = False
        if event.attendee.filter(id=self.request.user.id).exists():
            is_attendee = True

        return render(request, 'eventview.html',
                      {'event': event, 'is_attendee': is_attendee, })


# Good
# Notification that user has successfully registered for an event,
# passes them back to their event list with a button.
class EventReg(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventreg.html', {'event': event})


# Good
# Notification that a user has successfully left an event,
# passes them back to their event list with a button.
class EventUnReg(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventunreg.html', {'event': event})


# Good
# The code that adds or removes a user object
# from the attendee list of an Event.
class UserReg(View):
    def post(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        if event.attendee.filter(id=request.user.id).exists():
            event.attendee.remove(request.user)
            return render(request, 'eventunreg.html', {})
        else:
            event.attendee.add(request.user)
            return render(request, 'eventreg.html', {})


# Render a form so an event organizer can organize an event.
class EventEdit(View):
    def get(self, request):
        return render(request, 'eventedit.html', {'event_form': EventForm()})

    def post(self, request):
        event_form = EventForm(data=request.POST)

        if event_form.is_valid():
            event_form.instance.organizer = request.user
            event = event_form.save(commit=True)
        else:
            event_form = EventForm()

        return render(request, 'eventthanks.html', {'event': event})


# Working
# Thanks organizer for publishing a new event
class EventThanks(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventthanks.html', {'event': event})


# Allows an organizer to delete an event.
class EventDelete(View):
    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventdelete.html', {'event': event})


# Deletes the event from the confirmation page.
class ConfirmDelete(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

    def post(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)
        Event.objects.filter(event_name=event_name).delete()

        return render(request, 'confirmdelete.html', {'event': event})
