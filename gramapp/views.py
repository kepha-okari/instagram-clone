from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment,Like,Follow
from .forms import ImagePostForm,CommentForm

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
def single_image(request, photo_id):
    '''
    View funtion to display a particular image with its details
    '''
    image = Image.objects.get(id = photo_id)
    user_info = Profile.objects.get(user=image.user.id)#fetch the profile of the user who posted
    comments = Comment.objects.filter(post=image.id)
    upvotes = Like.objects.all().filter(post=image.id)
    likes = len(upvotes)
    return render(request, 'single-image.html', {'image':image, "user_info":user_info,"comments":comments, "likes":likes})


@login_required(login_url='/accounts/login')
def profile(request):
    '''
    View function to display the profile of the logged in user when they click on the user icon
    '''
    current_user = request.user# get the id of the current

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        info = Profile.objects.filter(user=current_user)

        pics = Image.objects.filter(user=request.user.id).all()

    except ObjectDoesNotExist:
            raise Http404()

    return render(request, 'my-profile.html', {"title":title,"current_user":current_user,"info":info, "pics":pics})




@login_required(login_url='/accounts/login')
def other_profile(request,prof_id):
    '''
    View function to display a profile information of other users
    '''
    current_user = request.user

    try:

        info = Profile.objects.filter(id=prof_id)

        pics = Image.objects.all().filter(user=prof_id)

        title = f'{request.user.username}\'s'

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'other-profile.html', {"title":title,"current_user":current_user,"info":info, "pics":pics})



@login_required(login_url='/accounts/login')
def new_post(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImagePostForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(profile)
    else:
        form = ImagePostForm()
    return render(request, 'new-post.html', {"form":form})



@login_required(login_url='/accounts/login/')
def new_comment(request, image_id):
    current_image = Image.objects.get(id=image_id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = current_user
            comment.post = current_image
            comment.save()
        return redirect('profileView')
    else:
        form = CommentForm()
    return render(request, 'new-comment.html', {"form": form, "current_image":current_image})



@login_required(login_url='/accounts/login')
def like(request,id):
    '''
    View function add a like to a post the current user has liked
    '''
    current_user = request.user

    current_image = Image.objects.get(id=id)

    like = Like(user=current_user,post=current_image,likes_number=int(1))

    like.save()

    return redirect(single_image,current_image.id)



@login_required(login_url='/accounts/register')
def follow(request,id):
    '''
    View function to add a profile to the current user's timeline
    '''
    current_user = request.user

    follow_profile = Profile.objects.get(id=id)

    following = Follow(user=current_user, profile=follow_profile)

    following.save()

    return redirect(timeline)
