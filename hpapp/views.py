from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event, Siteuser
from .forms import EventForm
from django import forms
import datetime


# Home page.
class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(event_date__gte=datetime.date.today()
                                    ).order_by('event_date')
    template_name = 'index.html'
    paginate_by = 5


# Logged in user's list of events they have already registered for.
class YourEventList(generic.ListView):
    model = Event
    template_name = 'yourevents.html'
    paginate_by = 5

    def get_queryset(self):
        your_event_list = Event.objects.filter(attendee=self.request.user
                                               ).filter(
                                                event_date__gte=datetime.
                                                date.today()
                                                ).order_by('event_date')
        return your_event_list


# Event organizer's list of events they have organized.
class EventOrg(generic.ListView):
    model = Event
    template_name = 'eventorg.html'
    paginate_by = 5

    def get_queryset(self):
        your_event_list = Event.objects.filter(organizer=self.request.user
                                               ).order_by('event_date')
        return your_event_list


# Owner control panel for approving event organizers, etc.
def OwnConPan(request):
    return render(request, 'ownconpan.html', {})


# Logged in user can view an event and either register for it if not
# already registered, and unregister if already registered.
class EventView(View):
    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        is_attendee = False
        if event.attendee.filter(id=self.request.user.id).exists():
            is_attendee = True
        is_closed = False
        if event.event_date_reg_close <= datetime.date.today():
            is_closed = True
#        elif event.number_of_attendees >= event.number_cars:
#            is_closed = True

        return render(request, 'eventview.html',
                      {'event': event, 'is_attendee': is_attendee,
                       'is_closed': is_closed})

    def post(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        is_attendee = False
        if event.attendee.filter(id=self.request.user.id).exists():
            is_attendee = True

        return render(request, 'eventview.html',
                      {'event': event, 'is_attendee': is_attendee, })


# Notification that user has successfully registered for an event,
# passes them back to their event list with a button.
class EventReg(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventreg.html', {'event': event})


# Notification that a user has successfully left an event,
# passes them back to their event list with a button.
class EventUnReg(View):
    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(request, 'eventunreg.html', {'event': event})


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
class EventCreate(View):
    def get(self, request):
        return render(request, 'eventcreate.html', {'event_form': EventForm()})

    def post(self, request):
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event_form.instance.organizer = request.user
            event = event_form.save(commit=True)
        else:

            return render(request, 'eventcreate.html',
                          {'event_form': event_form})

        return render(request, 'eventthanks.html', {'event': event})


# Allows organizer to edit an existing event.
class EventEdit(View):
    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        edit_form = EventForm(instance=event)

        return render(request, 'eventedit.html',
                      {'edit_form': edit_form, 'event': event})

    def post(self, request, event_name, *args, **kargs):
        event = Event.objects.get(event_name=event_name)

        if request.method == 'POST':
            edit_form = EventForm(request.POST, instance=event)
            if edit_form.is_valid():
                edit_form.save()
            else:
                edit_form = EventForm(instance=event)

                return render(request, 'eventedit.html',
                              {'event_form': edit_form,
                               'event': event})

            return render(request, 'eventthanks.html', {'event': event})

        else:
            event_form = EventForm(instance=event)


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


# Returns a list of attendees for a specific event.
class AttendeeList(View):
    def get(self, request, event_name, *args, **kwargs):
        event = get_object_or_404(Event, event_name=event_name)
        attendee_list = event.attendee.all().order_by('username')

        return render(request, 'attendeelist.html',
                      {'event': event, 'attendee_list': attendee_list})       
