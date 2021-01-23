from django.shortcuts import render
from .forms import DayCreateForm


def index(request):
    return render(request, 'diary/day_list.html')


def add(request):
    context = {
        'form': DayCreateForm
    }
    return render(request, 'diary/day_form.html', context)
