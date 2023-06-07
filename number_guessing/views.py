from django.shortcuts import render
from django.db.models import Avg

from .forms import NumberGuessForm
from .models import NumberGuess
import random


def number_guessing_view(request):
    sort_param = request.GET.get('sort', None)
    avg_correct = NumberGuess.objects.aggregate(Avg('is_correct'))['is_correct__avg']
    avg_number = NumberGuess.objects.aggregate(Avg('number'))['number__avg']
    context = {
        'avg_correct': avg_correct,
        'avg_number': avg_number,
        'number_guesses': NumberGuess.objects.all(),
        'condition': False,
        'translation': None
    }
    if sort_param is not None:
        context['condition'] = True
        sort_order = request.GET.get('order', None)
        number_guesses = NumberGuess.objects.order_by('-' * (sort_order == 'desc') + sort_param)
        context['number_guesses'] = number_guesses
        return render(request, 'number_guessing/result.html', context=context)
    if request.method == 'POST':
        form = NumberGuessForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('form is valid')
            guess = form.cleaned_data['guess']
            number = form.cleaned_data['number']
            is_correct = check_user_guess(number, guess)

            number_guess = NumberGuess.objects.create(
                number=number,
                guess=guess,
                is_correct=is_correct,
            )
            number_guess.save()

            translation = {'positive': 'положительное число!',
                           'negative': 'отрицательное число!',
                           'zero': 'ноль.'}
            context['translation'] = translation[guess]
            context['number_guesses'] = NumberGuess.objects.all()
            context['number_guess'] = number_guess
            return render(request, 'number_guessing/result.html', context=context)
    number = generate_random_number()
    form = NumberGuessForm(initial={'number': number})
    return render(request, 'number_guessing/guess.html', {'form': form, 'number': number})


def results_view(request):
    filter_value = request.GET.get('filter')

    if filter_value:
        number_guesses = NumberGuess.objects.filter(is_correct=filter_value)
    else:
        number_guesses = NumberGuess.objects.all()

    return render(request, 'number_guessing/.results.html', {'number_guesses': number_guesses})


def generate_random_number():
    return round(random.normalvariate(0, 1), 1)


def check_user_guess(number, guess):
    if number > 0 and guess == 'positive':
        return True
    elif number < 0 and guess == 'negative':
        return True
    elif number == 0 and guess == 'zero':
        return True
    return False
