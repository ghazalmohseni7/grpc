from django.shortcuts import render
from Database.models import Event
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework import status
from mongoengine import *
connection=connect("Event")
# Create your views here.


class ListEvents(APIView):
    def get(self,request):
        objs = json.loads(Event.objects().to_json())
        return Response({'data': objs}, status=status.HTTP_200_OK)



