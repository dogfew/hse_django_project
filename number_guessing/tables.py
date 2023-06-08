import django_tables2 as tables
from statistics import mean, stdev
from collections import Counter
from .models import NumberGuess


class MeanColumn(tables.Column):
    def render_footer(self, bound_column, table):
        rows = [bound_column.accessor.resolve(row) for row in table.data]
        mean_ = mean(rows) if len(rows) > 0 else 0
        std_ = stdev(rows) if len(rows) > 1 else 1
        min_ = min(rows) if len(rows) > 0 else 0
        max_ = max(rows) if len(rows) > 0 else 0
        return f"Mean: {round(mean_, 3)}, Std: {round(std_, 3)}, Min: {min_}, Max: {max_}"


class NumberColumn(tables.Column):
    def render_footer(self, bound_column, table):
        rows = [bound_column.accessor.resolve(row) for row in table.data]
        return f"N: {len(rows)}"


class GuessCountColumn(tables.Column):
    def render_footer(self, bound_column, table):
        rows = [bound_column.accessor.resolve(row) for row in table.data]
        return ', '.join(f"{k}: {v}" for k, v in Counter(rows).items())


class NumberGuessTable(tables.Table):
    footer_attrs = {"tf": {"bgcolor": '#eeffec'},
                    "td": {'bgcolor': '#fffaec'}}
    number = MeanColumn(attrs=footer_attrs)
    created_at = NumberColumn(attrs=footer_attrs)
    is_correct = MeanColumn(attrs=footer_attrs)
    guess = GuessCountColumn(attrs=footer_attrs)

    class Meta:
        model = NumberGuess
        template_name = "django_tables2/bootstrap.html"
        fields = ("number", "guess", "is_correct", "created_at")
