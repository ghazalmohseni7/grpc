from django.shortcuts import render
from DataBase.models import Type
from rest_framework.views import APIView
import json
from rest_framework.response import Response
from rest_framework import status
from mongoengine import *
connection=connect("Type")
from redis_micro import CacheRedis
from event_grpc import client

class ListType(APIView):
    def get(self,request):

        objs = json.loads(Type.objects().to_json())
        return Response({'data': objs}, status=status.HTTP_200_OK)


class List_Type_and_Event(APIView):
    def get(self,request):
        result="nothing to do"
        type_objs = Type.objects().to_json()
        redis_obj=CacheRedis()
        events=redis_obj.get("EventAll")
        print("from redis : ", events)
        if events:
            print("getting from redissssssssssssssssss")
            print(events)
            print(type(events))
            result=str(type_objs + str(events))
        else:
            print("redis nabood ")
            events=client.run()
            if events:
                print(events)
                print(type(events))
                result=str(type_objs + events)
            else:
                print("grpc ham nafrestad")


        return Response({'data': result}, status=status.HTTP_200_OK)