from .models import Page


def pages_context_processor(request):
    pages = Page.objects.filter(nav_position__gt=0).order_by('-nav_position')
    return {'pages': pages}