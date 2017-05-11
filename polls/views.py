from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# INDEX VIEW
def index(request):
  return HttpResponse('Index view reached')