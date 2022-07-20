from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from events.models import Event


def index(request):
    return HttpResponse("Hello world.")


def event_list(request):
    events = Event.objects.filter(created_date__lte=timezone.now()).order_by('event_date')
    return render(request, 'event_list.html', {'events': events})
