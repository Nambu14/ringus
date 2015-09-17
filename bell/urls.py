from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^record/', views.record, name='record'),
    url(r'^(?P<visitorId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<visitorId>[0-9]+)/results/$', views.results, name='messages'),
    url(r'^(?P<visitorId>[0-9]+)/message/$', views.message, name='message'),
]
