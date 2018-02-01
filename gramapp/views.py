from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile,Image
from .forms import ImagePostForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os


# Create your views here.
# def index(request):
#     return render(request, 'index.html')
# # def welcome(request):

@login_required(login_url='/accounts/login')
def index(request):
    images = Image.get_images()
    return render(request, 'index.html', {"images": images})


@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user# get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user.id)
        pics = Image.objects.filter(user=current_user.id)
        # pics = Image.get_images
        return render(request, 'profile.html', {"title":title,"current_user":current_user,"info":info, "pics":pics})

    except DoesNotExists:
        raise Http404()

@login_required(login_url='/accounts/register')
def new_post(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user
    '''
    current_user = request.user

    # current_profile = current_user.profile

    if request.method == 'POST':

        form = ImagePostForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            # post.profile = current_profile
            post.save()

            return redirect(profile, current_user.id)
    else:

        form = ImagePostForm()
        title = 'Create Post'

    return render(request, 'new-post.html', {"form":form})
