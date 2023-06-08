from .models import Page, LatexFormula


def pages_context_processor(request):
    pages = Page.objects.filter(nav_position__gt=0).order_by('-nav_position')
    formulas = LatexFormula.objects.order_by('-order')
    return {'pages': pages, 'formulas': formulas}