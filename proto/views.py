from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(http_method_names=['GET','POST','PUT'])
def echo(request,*args,**kwargs):
    return Response(request.data)