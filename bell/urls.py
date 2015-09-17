from django.conf.urls import url


from . import views


urlpatterns = [
    # This patterns are tested in order!!!
    url(r'^$', views.index, name='index'),
    url(r'^record/', views.record, name='record'),
    url(r'^(?P<visitId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<visitorId>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<visitorId>[0-9]+)/message/$', views.message, name='message'),
]
