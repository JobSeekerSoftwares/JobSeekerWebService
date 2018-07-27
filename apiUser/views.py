from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import TrabalhadorSerializer, EmpregadorSerializer
from .models import Empregador, Trabalhador
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class TrabalhadorViewSet(viewsets.ModelViewSet):
    queryset = Trabalhador.objects.all()
    serializer_class = TrabalhadorSerializer


class EmpregadorViewSet(viewsets.ModelViewSet):
    queryset = Empregador.objects.all()
    serializer_class = EmpregadorSerializer


class UserTrabalhadorCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self,request, format='json'):
        serializer = TrabalhadorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format='json'):
        try:
            idGmail = request.data['idGmail']
            person = Trabalhador.objects.all().filter(idGmail=idGmail).first()
        except Trabalhador.DoesNotExist:
            return HttpResponse(status=404)

        serializer = TrabalhadorSerializer(person, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEmpregadorCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self,request, format='json'):
        serializer = EmpregadorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format='json'):
        oldCargo = request.GET.get('oldCargo', '')
        print(oldCargo)
        try:
            idGmail = request.data['idGmail']
            person = Empregador.objects.all().filter(nome=oldCargo, idGmail=idGmail).first()
        except Empregador.DoesNotExist:
            return HttpResponse(status=404)

        serializer = EmpregadorSerializer(person, data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def person_search(request):
    """
    Retrieve, update or delete a code snippet.
    """
    idGmail = request.GET.get('idGmail', '')
    try:
        person = Trabalhador.busca.get_by_idGmail(idGmail)
    except Trabalhador.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TrabalhadorSerializer(person,  many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TrabalhadorSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        person.delete()
        return HttpResponse(status=204)


@csrf_exempt
def job_search(request, curriculo):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Empregador.busca.get_queryset(curriculo)
    except Empregador.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmpregadorSerializer(snippet,  many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpregadorSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def empregadores_list(request):
    if request.method == 'GET':
        empregadores = Empregador.objects.all()
        serializer = EmpregadorSerializer(empregadores, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpregadorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# Funcao principal que faz o get dos jobs parecidos com o curriculo
@csrf_exempt
def job_search2(request):
    """
    Retrieve, update or delete a code snippet.
    """
    curriculo = request.GET.get('curriculo', '')
    try:
        snippet = Empregador.busca.get_queryset(curriculo)
    except Empregador.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmpregadorSerializer(snippet,  many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpregadorSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def meus_empregos(request):
    """
    Retrieve, update or delete a code snippet.
    """
    idGmail = request.GET.get('idGmail', '')
    try:
        empregos = Empregador.objects.all().filter(idGmail=idGmail)
    except Empregador.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmpregadorSerializer(empregos,  many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmpregadorSerializer(empregos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
