from django.shortcuts import redirect
from django_filters.views import FilterView
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from .tables import SignTable
from .filters import SignFilter
from .forms import SignForm
from .models import Sign
from math import copysign


class FilteredSignView(SingleTableMixin, FilterView):
    table_class = SignTable
    model = Sign
    table_pagination = {"per_page": 10}
    filterset_class = SignFilter
    template_name = "sign_function/template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignForm()
        return context

    def post(self, request):
        form = SignForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            sign = copysign(1, number) * (1 - (number == 0))
            translation = {0: 'Ноль', -1: 'Отрицательное', 1: 'Положительное.'}
            sign_object = Sign.objects.create(
                condition=f"Дано число {number}. Определить, какое оно: положительное, отрицательное, или ноль.",
                number=number,
                sign=sign,
                sign_text=translation[sign],
            )
            sign_object.save()
            return redirect('/sign/?sort=-created_at')
