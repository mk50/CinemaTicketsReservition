from django import http
from django.db import router
from django.db.models.query import QuerySet
from django.http import response
from django.shortcuts import render
import rest_framework
from rest_framework.serializers import Serializer


from tickets.models import Guest
from . import views
from django.http.response import Http404, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status,filters
from rest_framework.response import Response
from rest_framework import generics,mixins,viewsets
def no_rest_model(request):

    guest=[
        {
         'id':1,
         'name':'mohamed',
         'mobile':123456,

    },
    {
     'id':2,
         'name':'mahmoudd',
         'mobile':4548524185,
     
    },
    {
            'id':3,
         'name':'islam',
         'mobile':18785648,

    }
    ]
    return JsonResponse(guest,safe=False)

def no_rest_from_model(request):
    guest=Guest.objects.all()
    response={
        "guest":list(guest.values('name','mobile'))
    }
    return JsonResponse(response)

@api_view(['GET','POST'])
def FBV_list(request):
    #GET
    if request.method=='GET':
        guest=Guest.objects.all()
        serializer=GuestSerializer(guest,many=True).data
        return Response(serializer)
        #post
    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk):
    try:
       guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET DETAILS
    if request.method=='GET':
        serializer=GuestSerializer(guest).data
        return Response(serializer)
    elif request.method=='PUT':
        #UPDATE
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#GET POST class based view
class CBV_list(APIView):
    def get(self,request):
        guest=Guest.objects.all()
        serializer=GuestSerializer(guest,many=True).data
        return Response(serializer)
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


#GET PUT DELETE class based view
class CBV_pk(APIView):

    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest)
        return Response(serializer.data)
    def put(self,request,pk):
        guest=self.get_object(pk)
        serializer=GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class mixin_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

class generic_list(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
class generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

 
class viewsets_guest(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backend=[filters.SearchFilter]
    search_fileds=['movie']

class viewsets_reversation(viewsets.ModelViewSet):
    queryset=Reversation.objects.all()
    serializer_class=ReversationSerializer

@api_view(['GET'])
def find_movie(request):
    movies=Movie.objects.filter(movie=request.data['movie'],
    hall=request.data['hall'])
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def new_reversation(request):
    movie=Movie.objects.get(movie=request.data['movie'],hall=request.data['hall']
    )
    guest=Guest()
    guest.name=request.data['name']
    guest.mobile=request.data['mobile']
    guest.save()

    reversation=Reversation()
    reversation.guest=guest
    reversation.movie=movie
    reversation.save()
    serializer=ReversationSerializer(reversation)
    return Response(serializer.data)