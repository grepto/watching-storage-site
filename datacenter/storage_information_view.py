from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.utills import get_visit_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in visits:
      non_closed_visits.append({
        'who_entered': visit.passcard.owner_name,
        'entered_at':visit.entered_at.strftime('%Y-%m-%d %H:%M:%S'),
        'duration':get_visit_duration(visit),
      })

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
