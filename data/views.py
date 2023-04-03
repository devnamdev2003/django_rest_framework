import io
from django.http import HttpResponse
from .models import StudentData
from .serializers import StudentApi
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


def home(request):

    # This function renders the home page for the API.
    return render(request, "api/index.html")


def index(request):

    # This function retrieves all student data and returns it in JSON format.
    if request.method == "GET":
        try:
            stu = StudentData.objects.all()
            serialze_data = StudentApi(stu, many=True)
            json_data = JSONRenderer().render(serialze_data.data)
            return HttpResponse(json_data,      content_type='application/json')
        except StudentData.DoesNotExist:
            res = {'message': ['does not exist']}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")


def fetch(request, i):

    # This function retrieves the student data with the given ID and returns it in JSON format.
    if request.method == "GET":
        try:
            stu = StudentData.objects.get(id=i)
            serialze_data = StudentApi(stu)
            json_data = JSONRenderer().render(serialze_data.data)
            return HttpResponse(json_data,      content_type='application/json')
        except StudentData.DoesNotExist:
            res = {'message': ['does not exist']}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def insert(request):

    # This function inserts new student data into the database.
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize_data = StudentApi(data=python_data)
        if serialize_data.is_valid():
            serialize_data.save()
            res = {'msg': ['data created']}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serialize_data.errors)
        return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def remove(request, i):

    # This function removes the student data with the given ID from the database.
    if request.method == "DELETE":
        try:
            stu = StudentData.objects.get(id=i)
            stu.delete()
            res = {'massage': ['data deleted']}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,  content_type="application/api")
        except StudentData.DoesNotExist:
            res = {'message': ['does not exist']}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")


@api_view(['GET', 'POST'])
def view(request, pk=None):

    # This function handles both GET and POST requests for student data.
    if request.method == "GET":
        if pk is not None:
            try:
                data = StudentData.objects.get(id=pk)
                serial = StudentApi(data)
                return Response(serial.data, status=status.HTTP_202_ACCEPTED)
            except StudentData.DoesNotExist:
                return Response({"msg": "Not exist"}, status=status.HTTP_204_NO_CONTENT)
        data = StudentData.objects.all()
        serial = StudentApi(data, many=True)
        return Response(serial.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == "POST":
        return Response({"msg": "post", "data": request.data})
