from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def index(request):
    return render(request, 'singlepage2/index.html')

texts = [
    'You choose the option 1. This is a good choice.',
    'You choose the option 2. This is also a good choice.',
    'You choose the option 3. This is a good choice too.'
]

def sections(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num-1])
    else:
        return Http404("No such section.")