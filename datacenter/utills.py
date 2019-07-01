from django.utils import timezone

def get_visit_leaved_at(visit):
  now = timezone.now()
  return visit.leaved_at if visit.leaved_at else now

def get_visit_duration(visit):
  leaved_at = get_visit_leaved_at(visit)
  return str(leaved_at - visit.entered_at)[:8].strip('.')