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
from api.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics, permissions, viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'offers': reverse('offer-list', request=request, format=format)
    })

###=====###
# Users
###=====###
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

###=====###
# Offers
###=====###
class OfferViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions over offer instances.
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)