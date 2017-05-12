from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# INDEX VIEW
def index(request):
  context = {
    'test_text': 'Hello World',
    'list': [1, 2, 3, 4, 5]
  }
  return render(request, 'polls/index.html', context)