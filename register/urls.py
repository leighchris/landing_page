from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from register import views

app_name = 'register'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homeform_view, name='home'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name ='edit_profile')
]

urlpatterns += staticfiles_urlpatterns()