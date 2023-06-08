from collections import Counter
from statistics import mean, stdev

import django_tables2 as tables
from .models import Sign


def stats(bound_column, table):
    rows = [bound_column.accessor.resolve(row) for row in table.data]
    mean_ = mean(rows) if len(rows) > 0 else 0
    std_ = stdev(rows) if len(rows) > 1 else 1
    min_ = min(rows) if len(rows) > 0 else 0
    max_ = max(rows) if len(rows) > 0 else 0
    return f"Mean: {round(mean_, 3)}, Std: {round(std_, 3)}, Min: {min_}, Max: {max_}"


class MeanColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return stats(bound_column, table)


class NumberColumn(tables.Column):
    def render_footer(self, bound_column, table):
        rows = [bound_column.accessor.resolve(row) for row in table.data]
        return f"N: {len(rows)}"


class GuessCountColumn(tables.Column):
    def render_footer(self, bound_column, table):
        rows = [bound_column.accessor.resolve(row) for row in table.data]
        return ',   '.join(f"{k}: {v}" for k, v in Counter(rows).items())


footer_attrs = {"tf": {"bgcolor": '#eeffec'},
                "th": {'bgcolor': '#ffecec'},
                "td": {'bgcolor': '#fffaec'}}
for key in footer_attrs:
    footer_attrs[key].update({
    })


class SignTable(tables.Table):
    condition = NumberColumn(attrs=footer_attrs)
    sign = GuessCountColumn(attrs=footer_attrs)
    number = MeanColumn(attrs=footer_attrs)
    sign_text = tables.Column(attrs=footer_attrs)
    created_at = tables.Column(attrs=footer_attrs, orderable=True)

    class Meta:
        model = Sign
        template_name = "django_tables2/bootstrap.html"
        fields = ("created_at", "condition", "number", "sign", "sign_text")