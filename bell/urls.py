from django.conf.urls import url


from . import views


urlpatterns = [
    # This patterns are tested in order!!!
    url(r'^$', views.index, name='index'),
    url(r'^record/', views.record, name='record'),
    url(r'^visitors/(?P<visitorId>[0-9]+)/$', views.visitor_details, name='visitorDetails'),
    url(r'^visitors/', views.visitors_management, name='visitorManagement'),
    url(r'^(?P<visitId>[0-9]+)/$', views.visit_detail, name='visit_detail'),
    url(r'^(?P<visitorId>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<visitorId>[0-9]+)/message/$', views.message, name='message'),
]
