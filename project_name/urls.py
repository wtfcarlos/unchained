from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += [
   		 (r'^media/(?P<path>.*)$',
   		 'django.views.static.serve',
   		 {'document_root': settings.MEDIA_ROOT}),
	]
