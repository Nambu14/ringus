from django.conf.urls import url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from bell import views


urlpatterns = [
    # This patterns are tested in order!!!
    url(r'^$', views.index, name='index'),
    url(r'^visit_record/', views.visit_record, name='visit_record'),
    url(r'^visitors/(?P<visitor_id>[0-9]+)/$', views.visitor_details, name='visitor_details'),
    url(r'^visitors/', views.visitors_management, name='visitor_management'),
    url(r'^(?P<visit_id>[0-9]+)/$', views.visit_detail, name='visit_detail'),
    url(r'^(?P<visitor_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<visitor_id>[0-9]+)/message/$', views.message, name='message'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^editvisitor/(?P<pk>[0-9]+)/$', VisitorUpdate.as_view(), name='update_visitor'),
    url(r'^createvisitor/$', VisitorCreate.as_view(), name='create_visitor'),
    # REST patterns
    url(r'^restvisitor/(?P<pk>[0-9]+)/$', views.VisitorDetail.as_view()),
    url(r'^restvisitor/$', views.VisitorList.as_view()),
    url(r'^restvisit/(?P<pk>[0-9]+)/$', views.VisitDetail.as_view()),
    url(r'^restvisit/$', views.VisitList.as_view()),
    url(r'^restmessage/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
    url(r'^restmessage/$', views.MessageList.as_view()),
    url(r'^restnotification/(?P<pk>[0-9]+)/$', views.NotificationDetail.as_view()),
    url(r'^restnotification/$', views.NotificationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)