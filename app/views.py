from django.conf import settings
from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    return render_to_response('main.html')