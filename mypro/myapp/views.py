from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "post method only"})
    elif request.method == 'GET':
        return Response({"message": "get method only"})
    elif request.method == 'PUT':
        return Response({"message": "put method only"})
    elif request.method == 'PATCH':
        return Response({"message": "patch method only"})
    elif request.method == 'DELETE':
        return Response({"message": "delete method only"})
    
