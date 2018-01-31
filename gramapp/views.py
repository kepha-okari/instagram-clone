from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')
# def welcome(request):
