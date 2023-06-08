from django import forms


class NumberGuessForm(forms.Form):
    guess_choices = [
        ('positive', 'Положительное'),
        ('negative', 'Отрицательное'),
        ('zero', 'Ноль'),
    ]
    guess = forms.ChoiceField(choices=guess_choices, widget=forms.RadioSelect, label="Какое оно?")
    number = forms.FloatField(widget=forms.HiddenInput())
