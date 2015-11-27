from django.conf.urls import patterns, url

urlpatterns = patterns('overloader.views',
    url(r'.*', 'index', name='index')
)
