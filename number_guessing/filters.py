from django_filters import FilterSet
from .models import NumberGuess


class NumberGuessFilter(FilterSet):
    class Meta:
        model = NumberGuess
        fields = {"number": ["exact", "contains"], "guess": ["exact"], "is_correct": ['exact']}