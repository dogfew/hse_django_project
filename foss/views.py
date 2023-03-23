import datetime

from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .forms import ContactForm, OpinionForm
from .models import Person, Opinion, Task


# Create your views here.

class SimpleHandler:
    def __init__(self, target: str):
        """
        :param target: html-page.
        """
        self.target = target

    def __call__(self, request: HttpRequest):
        return render(request, self.target, {'page_title': self.target.split('.')[0].capitalize()})


def get_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.__dict__['cleaned_data']
            data['date'] = timezone.now()
            person = Person(**data)
            person.save()
            return HttpResponse(f"Информация записана!<br>{data}<br><a href=''>Назад</a>")
    form = ContactForm()
    return render(request, 'forms.html', {'form': form, 'page_title': 'Contact'})


def get_opinion(request):
    query_results = Opinion.objects.all()
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            data = form.__dict__['cleaned_data']
            data['date'] = timezone.now()
            new_opinion = Opinion(**data)
            new_opinion.save()
            return HttpResponseRedirect('')
    else:
        form = OpinionForm()
    return render(request,
                  'opinion.html',
                  {
                      'form': form,
                      'query_results': query_results,
                      'page_title': 'Form'
                  }
                  )


def interactive_controller(request):
    if request.method == 'POST':
        try:
            expected_prime = int(request.POST.get('expected_prime'))
            got_prime = int(request.POST.get('next_prime'))
            prime_num = int(request.POST.get('prime_num'))
            task = Task(expected_value=expected_prime, answer=got_prime, prime_num=prime_num)
            task.save()
            return HttpResponse(f"Информация записана!"
                                f"<br>Ваш ответ: {got_prime}"
                                f"<br>Правильный ответ: {expected_prime}"
                                f"<br>Номер {prime_num}"
                                f"<br><a href=''>Назад</a>")
        except Exception as e:
            print(e)
            return HttpResponse(f"Информация не записана!<br>Неверный формат ввода.<br>"
                                f"<br><a href=''>Назад</a>")
    return render(request, 'interactive.html', {'page_title': 'Calculator'})
