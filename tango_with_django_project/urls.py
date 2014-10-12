from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       
    url(r'^admin/', include(admin.site.urls)),

    url(r'^rango/', include('rango.urls')),

)
