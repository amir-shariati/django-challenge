from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import (
    Stadium, Match, Seat, TicketPurchase
)


class StadiumSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Stadium
        fields = '__all__'


class MatchSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
        expandable_fields = {
            'stadium': StadiumSerializer,
        }


class SeatSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
        expandable_fields = {
            'match': MatchSerializer,
        }


class TicketPurchaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TicketPurchase
        fields = '__all__'
        expandable_fields = {
            'seat': SeatSerializer,
        }
