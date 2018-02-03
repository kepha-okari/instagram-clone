from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required #restricting access to images for only registered users
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='timeline'),
    url(r'^profile/',views.profile, name='profileView'),
    url(r'^other/profile/(\d+)',views.other_profile, name='otherProfile'),
    url(r'^post/',views.new_post, name='postImage'),
    url( r'^comment/(\d+)', views.new_comment, name='Comment'),
    url(r'^single/image/(\d+)', views.single_image, name='singleImage'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
