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

        return render(
            request,
            'eventview.html',
            {'event': event}
        )


class EventReg(View):

    def get(self, request, event_name, *args, **kargs):
        event = get_object_or_404(Event, event_name=event_name)

        return render(
            request,
            'eventreg.html',
            {'event': event}
        )

    def post(self, request, even_name, *args, **kargs):

        car_form = Form(data=reques.post)

        if car_form.is_valid():
            car = car_form.save(commit=False)
            car.car_owner = request.user.username
            car.event = event_name
        else:
            car_form = Form()

        return render(
            request,
            'index.html'
        )
