from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Offer, Notification


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'username', 'email', 'is_staff')

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'name', 'goal_qnt', 'price', 'discount_perc', 'expedition_price')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'message', 'user', 'read', 'pub_date')