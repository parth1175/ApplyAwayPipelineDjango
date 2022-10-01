from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from demoapp.models import data
from demoapp.forms import UploadBookForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from bs4 import BeautifulSoup
from django.template import loader
from django.urls import reverse
from rest_framework import generics
from .serializers import BookSerializer
from .models import data
import os
import boto3
import botocore

class BookList(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = data.objects.all()
    serializer_class = BookSerializer


def make_txt(data: str, task_id: str):
    """Produce csv file with generated fake data and name it as task id."""

    file_path = os.path.normpath(f"{task_id}.txt")
    with open(file=file_path, mode="wb+") as txt_file:
        print("writing data to file")
        txt_file.write(bytes(data, encoding='utf-8'))
    return file_path


def upload_file(file_path, bucket, object_name=None):
    """Upload a file to an S3 bucket."""
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client("s3")

    # raw_file = bytes(file.getvalue())  # convert to bytes
    with open(file_path, 'rb') as file:
        raw_file = file.read()
    text = "hello mfers"
    raw_file = bytes(text, encoding='utf8')

    try:
        response = s3_client.put_object(Bucket=bucket, Key=object_name, Body=raw_file)
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True


@csrf_exempt
def home(request):
    print("routed to function")
    if request.method == 'POST':
        print("method was post")
        reqs = request.body.decode('utf-8')
        try:
            reqs[:5]
            # take the whole reqs variable and write to file
            upload_file(make_txt(reqs, "nine"), "webextendev", "mykey3")

            return JsonResponse(
                {
                "success":True,
                "url": reqs[:5]
                }
            )
        except KeyError:
            print("wrong!")
    else:
        print("This is a GET request")
        return 0;
