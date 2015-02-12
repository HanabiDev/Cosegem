from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = patterns('',
	url(r'', include('two_factor.urls', 'two_factor')),
	url(r'', include('user_sessions.urls', 'user_sessions')),
    #url(r'^', include('ursus.urls')),
    #url(r'^cuenta/', include('ursus_auth.urls', 'ursus_auth')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

