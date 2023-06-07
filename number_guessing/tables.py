import django_tables2 as tables
from statistics import mean, stdev
from .models import NumberGuess


def stats(bound_column, table):
    rows = [bound_column.accessor.resolve(row) for row in table.data]
    mean_ = mean(rows)
    std_ = stdev(rows)
    min_ = min(rows)
    max_ = max(rows)
    return f"Mean: {round(mean_, 3)}, Std: {round(std_, 3)}, Min: {min_}, Max: {max_}"


class MeanColumn(tables.Column):
    def render_footer(self, bound_column, table):
        return stats(bound_column, table)


class NumberGuessTable(tables.Table):
    number = MeanColumn()
    is_correct = MeanColumn()

    class Meta:
        model = NumberGuess
        template_name = "django_tables2/bootstrap.html"
        fields = ("number", "guess", "is_correct", "created_at")
    # def render_row_number(self):
    #     return f"Row {next(self.counter)}"
    # def paginate(self, *args, **kwargs):
    #     return 10