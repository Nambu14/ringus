from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from .models import Visitor, Visit
# Create your views here.


def index(request):
    return render(request, 'bell/index.html')


def visit_detail(request, visit_id):
    # try:
    #     visitor = Visitor.objects.get(pk=visitorId)
    # except Visitor.DoesNotExist:
    #     raise Http404("Visitor does not exist")
    visit = get_object_or_404(Visit, pk=visit_id)
    return render(request, 'bell/visit_detail.html', {'visit': visit})


def visitors_management(request):
    visitors_list = Visitor.objects.order_by('-name')
    context = RequestContext(request, {
        'visitors_list': visitors_list,
    })
    return render(request, 'bell/visitors_management.html', context)


def visitor_details(request, visitor_id):
    visitor = get_object_or_404(Visitor, pk=visitor_id)
    return render(request, 'bell/visitor_detail.html', {'visitor': visitor})


def results(request, visitor_id):
    response = "you are looking at the results of visitor %s."
    return HttpResponse(response % visitor_id)


def message(request, visitor_id):
    return HttpResponse("you are leaving a message on visitor %s." % visitor_id)


def visit_record(request):
    latest_visits_list = Visit.objects.order_by('-date')
    # template = loader.get_template('bell/visit_record.html')
    context = RequestContext(request, {
        'latest_visits_list': latest_visits_list,
    })
    # return HttpResponse(template.render(context))
    return render(request, 'bell/visit_record.html', context)
