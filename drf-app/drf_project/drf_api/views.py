from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#
def index(request):
    if (request.method == 'GET'):
        return render(request, 'drf_api/index.html')
#
def testApi(request):
    if (request.method == 'GET'):
        class testAPIView(generics.ListAPIView):
            queryset = render(request, 'drf_api/index.html')
            serializer_class = testSerializer;
