from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile, Offer, Notification


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    offers = serializers.HyperlinkedRelatedField(many=True, view_name='offer-detail', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'email', 'is_staff', 'offers')

class OfferSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Offer
        fields = ('url', 'id', 'name', 'goal_qnt', 'price', 'discount_perc', 'expedition_price', 'user')

class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Notification
        fields = ('id', 'message', 'user', 'read', 'pub_date')