from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Publication, User
from .models import Shelves
from .models import Users
# Create your views here.
from .serializers import PublicationSerializer, UserSerializer
from .serializers import UsersSerializer
from .serializers import ShelvesSerializer


def publist(request):
    if request.method == 'GET':
        pubs = Publication.objects.all()
        serializer = PublicationSerializer(pubs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.POST)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['name'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
"""
def usrlist(request):
    if request.method == 'GET':
        pubs = Users.objects.all()
        serializer = UsersSerializer(pubs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""


def shelist(request):
    if request.method == 'GET':
        pubs = Shelves.objects.all()
        serializer = ShelvesSerializer(pubs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShelvesSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name']
    search_fields = ['=name', 'intro']
    ordering_fields = ['name', 'id']
    ordering = ['id']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)



class PublicationsViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['ISN', 'title']
    search_fields = ['=title', 'id']
    ordering_fields = ['title', 'ISN']
    ordering = ['ISN']
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
