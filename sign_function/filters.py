from django_filters import FilterSet
from .models import Sign


class SignFilter(FilterSet):
    class Meta:
        model = Sign
        fields = {"number": ["exact", "contains"], "sign": ["exact"], "sign_text": ['exact']}