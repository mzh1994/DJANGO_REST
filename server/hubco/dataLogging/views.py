from datetime import date
from sys import excepthook
from django.shortcuts import render,redirect
from django.http import HttpResponse
from numpy import record
from .models import data_input_table,app_daily_stats, kks_description
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import serializers, viewsets
from rest_framework.response import Response
import json
from sqlalchemy import create_engine
import pandas as pd
from .generate_report_data import generate_daily_report
import datetime
from .load_kks_data_table import load_kks_table
from .serializers import data_input_table_serilaizer,app_daily_stats_serilaizer,kks_description_serilaizer
from rest_framework.renderers import JSONRenderer
# making connection
# conn_str = 'postgresql://gveoaihnqvuuvj:dfe4ed4802ec0afa6cca854eb97b5e5d9a3f1f0bbae6ddba7f7585004f50363c@ec2-34-204-128-77.compute-1.amazonaws.com:5432/dvifbu9viiudm'
# engine = create_engine(conn_str)
conn_str = 'postgresql://postgres:password@localhost:5432/test_db'
engine = create_engine(conn_str)
# Create your views here.

#rest framework views

class input_data_ViewSet(viewsets.ModelViewSet):
    queryset = data_input_table.objects.all().order_by('-date')
    serializer_class = data_input_table_serilaizer

@api_view(['POST'])
def insert_input_data(request):
    if request.method == 'POST':
        for obj in request.data: #assuming you are posting a 'list' of objects
            data_input_table.objects.create(name=obj.name, value=obj.value, unit=obj.unit)
    return redirect('url of data_input_table List View')

class app_daily_stats_ViewSet(viewsets.ModelViewSet):
    queryset = app_daily_stats.objects.all().order_by('-date','shift')
    serializer_class = app_daily_stats_serilaizer

class kks_description_ViewSet(viewsets.ModelViewSet):
    queryset = kks_description.objects.all()#.order_by('id')
    serializer_class = kks_description_serilaizer