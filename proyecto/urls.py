from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^plus/(\d+)$','app.views.plus', name='plus'),
    url(r'^minus/(\d+)$','app.views.minus', name='minus'),
    url(r'^add/$','app.views.add', name='add'),

   
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
