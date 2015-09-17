from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from .models import Visitor, Visit
# Create your views here.


def index(request):
    return render(request, 'bell/index.html')


def detail(request, visitId):
    # try:
    #     visitor = Visitor.objects.get(pk=visitorId)
    # except Visitor.DoesNotExist:
    #     raise Http404("Visitor does not exist")
    visit = get_object_or_404(Visit, pk=visitId)
    return render(request, 'bell/detail.html', {'visit': visit})


def results(request, visitorId):
    response = "you are looking at the results of visitor %s."
    return HttpResponse(response % visitorId)


def message(request, visitorId):
    return HttpResponse("you are leaving a message on visitor %s." % visitorId)


def record(request):
    latest_visits_list = Visit.objects.order_by('-date')
    # template = loader.get_template('bell/record.html')
    context = RequestContext(request, {
        'latest_visits_list': latest_visits_list,
    })
    # return HttpResponse(template.render(context))
    return render(request, 'bell/record.html', context)
