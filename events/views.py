from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking, Expense, Feedback

def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})