import json
from django.db import models
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import  status
from .serializers import FileSerializer, DataSerializer
from django.core.serializers import serialize
from .models import Data
import pandas as pd
from .models import File
import os
from backend.settings import MEDIA_ROOT
from django.utils.dateparse import parse_date
import datetime
import json

from baggageai import serializers


class FileView(APIView,models.Model):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):

    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
        
        file_serializer.save()
        
        filename= os.path.join(MEDIA_ROOT ,str(File.objects.last().file))
        df = pd.read_csv(filename)
        for i in range(len(df)):
            d = Data(
                image_name = df.iloc[i].image_name,
                object_detected = df.iloc[i].objects_detected,
                timestamp = parse_date(df.iloc[i].timestamp)
            )
            d.save()
        return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self,request):
        try:
            dateStart = request.data.get('dateStart')
            dateEnd =  request.data.get('dateEnd')
            d=Data.objects.filter(timestamp__range=[dateStart, dateEnd])
            allitems = json.loads(serialize('json',d))
            return Response({'data':allitems})

        except Exception as e:
            print(e)
            return Response({'data':"something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        return Response({"data":"api"})
        
        

