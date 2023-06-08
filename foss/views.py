from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.template import Template, Context

from .forms import ContactForm, OpinionForm
from .models import Person, Opinion, Task, Page, LatexFormula, CodeExample, SoftExample


# Create your views here.
def start(request):
    return redirect('/index')


def render_page_content(content, context):
    template = Template(content)
    rendered_content = template.render(Context(context))
    context['rendered_content'] = rendered_content


def page_detail_view(request, nav=''):
    form = None
    page = Page.objects.get(nav=nav)
    context = {'page': page,
               'nav': nav,
               'form': form}
    if nav == 'formulas':
        context['formulas'] = LatexFormula.objects.all()
    elif nav == 'codes':
        context['codes'] = CodeExample.objects.order_by('order')
    elif nav =='about':
        context['programms'] = SoftExample.objects.all()
    render_page_content(page.content, context)
    match page.form_type:
        case 'contact':
            return get_contact(request, context)
        case 'opinion':
            return get_opinion(request, context)
        case 'interactive':
            return interactive_controller(request, context)
        case _:
            pass
    return render(request, 'base.html', context=context)


def get_contact(request, context):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.__dict__['cleaned_data']
            data['date'] = timezone.now()
            person = Person(**data)
            person.save()
            data_out = '<br>'.join([f"<b>{key}:</b> {value}" for key, value in data.items()])
            render_page_content(

                f"<div class='table'><h3>Информация записана!</h3><br>{data_out}<br></div><button><a href=''>Назад</a></button>",
                context)
            context['page'].has_form = False
            return render(request, 'base.html', context=context)
    form = ContactForm()
    render_page_content(context['page'].content, context)
    context['form'] = form
    return render(request, 'base.html', context=context)


def get_opinion(request, context):
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
            form = OpinionForm(query_results)
    else:
        form = OpinionForm()
    context['query_results'] = query_results
    context['form'] = form
    render_page_content(context['page'].content, context)
    return render(request, 'base.html', context)


def interactive_controller(request, context):
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
    render_page_content(context['page'].content, context)
    return render(request, 'base.html', context)
