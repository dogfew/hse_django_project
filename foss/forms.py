from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='')
    second_name = forms.CharField(max_length=100, label='')
    phone = forms.CharField(max_length=100, empty_value='Enter your phone!', label='')
    email = forms.EmailField(label='')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'first name'
        self.fields['second_name'].widget.attrs['placeholder'] = 'second name'
        self.fields['phone'].widget.attrs['placeholder'] = 'phone'
        self.fields['email'].widget.attrs['placeholder'] = 'email'


class OpinionForm(forms.Form):
    distro_name = forms.CharField(max_length=100, label='')
    rate = forms.IntegerField(label='', min_value=0, max_value=10)
    opinion = forms.CharField(max_length=100, label='')

    def __init__(self, *args, **kwargs):
        super(OpinionForm, self).__init__(*args, **kwargs)
        self.fields['distro_name'].widget.attrs['placeholder'] = 'distro_name'
        self.fields['rate'].widget.attrs['placeholder'] = 'rate'
        self.fields['opinion'].widget.attrs['placeholder'] = 'opinion'


