from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required #restricting access to images for only registered users
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index,name='homePage'),
    url(r'^profile/(\d+)',views.profile, name='profileView'),
    url(r'^post/',views.new_post, name='postImage'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
