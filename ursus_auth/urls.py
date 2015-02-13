from django.conf.urls import patterns, include, url
from django.contrib import admin

from two_factor.urls import urlpatterns as tf_urls
#from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

from views import (OwnDisableView, OwnSetupView, OwnLoginView)


urlpatterns = patterns(
    '',
    url(r'^$', 'ursus_auth.views.home', name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^desactivar-otp/$', OwnDisableView.as_view(), name='disable_otp'),
    url(r'^activar-otp/$', OwnSetupView.as_view(), name='enable_otp'),
    
    
    url(r'', include(tf_urls, 'two_factor')),
    url(r'', include('user_sessions.urls', 'user_sessions')),
)
