from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required #restricting access to images for only registered users
from . import views

urlpatterns = [
    url(r'^$',views.index,name='homePage'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
