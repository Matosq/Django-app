from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^show_all/$','nowa.views.nowa'),
    url(r'^(?P<article_id>\d+)/$','nowa.views.article')
)