from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .serializers import *
from forms import ContactForm
from django.core.mail import send_mail
from django.views.generic.edit import UpdateView, CreateView
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
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
    visitors_list = Visitor.objects.order_by('surname')
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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['example@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'bell/contact.html', {'form': form})


class VisitorUpdate(UpdateView):
    model = Visitor
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = 'http://127.0.0.1:8000/bell/visitors/'


class VisitorCreate(CreateView):
    model = Visitor
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = 'http://127.0.0.1:8000/bell/visitors/'


# REST code
class VisitorList(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


'''
@api_view(['GET', 'POST'])
def visitor_list(request, format=None):
    """
    List all visitors or create a new visitor
    """
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def visitor_detail(request, pk, format=None):
    """
    Retrieve, update or delete any Visitor instance
    """
    try:
        visitor = Visitor.objects.get(pk=pk)
    except Visitor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request .method == 'GET':
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VisitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VisitorList(APIView):
    """
    List all visitors, or create a new visitor
    """

    def get(self, request, format=None):
        visitors = Visitor.objects.all()
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VisitorDetail(APIView):
    """
    Retrieve, update or delete a visitor instance
    """

    def get_object(self, pk):
        try:
            return Visitor.objects.get(pk=pk)
        except Visitor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        visitor = self.get_object(pk)
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        visitor = self.get_object(pk)
        serializer = VisitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        visitor = self.get_object(pk)
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VisitorList(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class VisitorDetail(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''