from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comment,Like,Follow
from .forms import ImagePostForm,CommentForm,ProfileForm

from wsgiref.util import FileWrapper
import mimetypes
from django.conf import settings
import os

@login_required(login_url='/accounts/login')
def index(request):
    # images = Image.get_images()
    current_user = request.user

    title = 'Timeline'

    # user_info = Profile.objects.get(user=current_user.id)

    grammers = Profile.get_profiles

    following = Follow.get_following(current_user.id)

    images = []
    for followed in following:
        # get profile id for each and use it to find user id
        profiles = Profile.objects.filter(id=followed.profile.id)
        for profile in profiles:
            post = Image.objects.filter(user=profile.user)

            for image in post:
                images.append(image)

    return render(request, 'index.html', {"images": images, "title": title, "following": following, "user": current_user, "grammers":grammers })


@login_required(login_url='/accounts/login')
def single_image(request, photo_id):
    '''
    View funtion to display a particular image with its details
    '''
    image = Image.objects.get(id = photo_id)
    user_info = Profile.objects.get(user=image.user.id)#fetch the profile of the user who posted
    comments = Comment.objects.filter(post=image.id)
    validate_vote = Like.objects.filter(user=request.user,post=photo_id).count()
    upvotes = Like.get_post_likes(image.id)
    likes = len(upvotes)
    return render(request, 'single-image.html', {'image':image, "user_info":user_info,"comments":comments, "likes":likes, "validate_vote":validate_vote})

@login_required(login_url='/accounts/login')
def manage_image(request, photo_id):
    '''
    View funtion to display a particular image with its details
    '''
    image = Image.objects.get(id = photo_id)
    user_info = Profile.objects.get(user=image.user.id)#fetch the profile of the user who posted
    comments = Comment.objects.filter(post=image.id)
    validate_vote = Like.objects.filter(user=request.user,post=photo_id).count()
    upvotes = Like.get_post_likes(image.id)
    likes = len(upvotes)
    return render(request, 'manage-image.html', {'image':image, "user_info":user_info,"comments":comments, "likes":likes, "validate_vote":validate_vote})



@login_required(login_url='/accounts/login')
def delete_post(request,image_id):
    '''
    View function to delete an image post
    '''
    remove = Image.objects.get(id = image_id)
    remove.delete()
    return  redirect(index)





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

    except:

        title = f'{current_user.username}\'s'

        pics = Image.objects.filter(user=request.user.id).all()

        info = Profile.objects.filter(user=7)

    return render(request, 'my-profile.html', {"title":title,"current_user":current_user,"info":info, "pics":pics})




@login_required(login_url='/accounts/login')
def other_profile(request,prof_id):
    '''
    View function to display a profile information of other users
    '''
    current_user = request.user

    try:

        info = Profile.objects.filter(id=prof_id)

        follow_profile = Profile.objects.get(id=prof_id)

        check_if_following = Follow.objects.filter(user=current_user, profile=follow_profile).count()

        pics = Image.objects.all().filter(user_id=prof_id)
        nbr = pics.count()

        title = f'{request.user.username}\'s'

    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'other-profile.html', {"title":title,"nbr":nbr,"current_user":current_user,"info":info, "pics":pics, "check_if_following":check_if_following})



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


@login_required(login_url='/accounts/login')
def create_profile(request):
    '''
    View function to create and update the profile of the user
    '''
    current_user = request.user

    profiles = Profile.objects.filter(user=current_user ).count()

    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid:

            if profiles == 0:
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
            else:
                record = Profile.objects.filter(user=current_user )
                record.delete()
                k = form.save(commit=False)
                k.user = current_user
                k.save()
                return redirect(profile)
    else:
        form = ProfileForm()
    return render(request, 'update-profile.html', {"form":form})


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
        return redirect(single_image,current_image.id)
    else:
        form = CommentForm()
    return render(request, 'new-comment.html', {"form": form, "current_image":current_image})


@login_required(login_url='/accounts/login')
def like(request,id):
    '''
    View function add a like to a post the current user has liked
    '''
    current_user = request.user #argument must be a string, a bytes-like object or a number, not 'Profile'

    current_image = Image.objects.get(id=id)

    validate_vote = Like.objects.filter(user=current_user,post=current_image).count()

    if validate_vote == 0:

        like = Like(user=current_user,post=current_image,likes_number=int(1))
        like.save()

    else:
        remove_like = Like.objects.filter(user=current_user,post=current_image)
        remove_like.delete()


    return redirect(single_image,current_image.id)



@login_required(login_url='/accounts/login')
def follow(request,id):
    '''
    View function add frofiles of other users to your timeline
    '''
    current_user = request.user

    follow_profile = Profile.objects.get(id=id)

    check_if_following = Follow.objects.filter(user=current_user, profile=follow_profile).count()

    if check_if_following == 0:

        following = Follow(user=current_user, profile=follow_profile)

        following.save()
    else:
        pass

    return redirect(index)


@login_required(login_url='/accounts/login')
def unfollow(request,id):
    '''
    View function unfollow other users
    '''
    current_user = request.user

    follow_profile = Profile.objects.get(id=id)

    following = Follow.objects.filter(user=current_user, profile=follow_profile)
    # following = Follow(user=current_user, profile=follow_profile)
    for item in following:
        item.delete()

    return redirect(index)
