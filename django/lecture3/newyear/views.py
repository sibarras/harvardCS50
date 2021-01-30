from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    date = datetime.now()
    new_year = date.month == 1 and date.day == 1

    return render(request, 'newyear/index.html', {
        'newyear': new_year
    })