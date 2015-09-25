from django.conf.urls import url
from .views import *


from . import views


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
]
