# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from core.models import Offer, Notification
from api.serializers import OfferSerializer, NotificationSerializer, UserSerializer

# Create your views here.
#@csrf_exempt
@api_view(['GET', 'POST'])
def offer_list(request):
    """
    List all offers, or create a new snippet.
    """
    if request.method == 'GET':
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OfferSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def offer_detail(request, pk):
    """
    Retrieve, update or delete an offer.
    """
    try:
        offer = Offer.objects.get(pk=pk)
    except Offer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OfferSerializer(offer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OfferSerializer(offer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        offer.delete()
        return HttpResponse(status=204)
