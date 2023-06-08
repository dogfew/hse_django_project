from django import forms


class SignForm(forms.Form):
    number = forms.FloatField(label="Введите число, чтобы определить, положительное оно, отрицательное или ноль.")
