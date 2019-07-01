from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.utills import get_visit_duration, get_visit_leaved_at

def is_visit_long(visit, minutes=60):
  entered_at = visit.entered_at
  leaved_at = get_visit_leaved_at(visit)
  return ((leaved_at - entered_at).seconds//60)%60 > minutes

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
      duration = get_visit_duration(visit)
      this_passcard_visits.append({
        'entered_at': visit.entered_at,
        'duration': duration,
        'is_strange': is_visit_long(visit)
      })
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
