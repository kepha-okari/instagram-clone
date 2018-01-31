from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Image

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os


# Create your views here.
# def index(request):
#     return render(request, 'index.html')
# # def welcome(request):
def index(request):
    images = Image.get_images()
    return render(request, 'index.html', {"images": images})


@login_required(login_url='/accounts/register')
def profile(request,id):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user# get the id of the current user

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Image.objects.filter(user=current_user.id)

        return render(request, 'profile.html', {"title":title,"current_user":current_user,"info":info})

    except DoesNotExists:
        raise Http404()
