from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^$', 'users.views.home', name='home'),
    url(r'^nuevo/$', 'users.views.new_user', name='new'),
    url(r'^ver/(?P<user_id>\d+)/$', 'users.views.profile', name='profile'),
    url(r'^editar/(?P<user_id>\d+)/$', 'users.views.edit_user', name='edit'),
    url(r'^bloquear/(?P<user_id>\d+)/$', 'users.views.toggle_lock', name='block'),
    url(r'^desbloquear/(?P<user_id>\d+)/$', 'users.views.toggle_lock', name='unblock'),
    
)
