from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import (
    Stadium, Match, Seat, TicketPurchase
)
from .serializers import (
    StadiumSerializer, MatchSerializer, SeatSerializer, TicketPurchaseSerializer
)


class StadiumListView(generics.ListCreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(StadiumListView, self).dispatch(*args, **kwargs)


class MatchListView(generics.ListCreateAPIView):
    queryset = Match.objects.select_related('stadium').all()
    serializer_class = MatchSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(MatchListView, self).dispatch(*args, **kwargs)


class SeatListView(generics.ListCreateAPIView):
    queryset = Seat.objects.select_related('match').all()
    serializer_class = SeatSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(SeatListView, self).dispatch(*args, **kwargs)


# Todo: using Low-Level Cache API, check or get seat_match_hash_id.
#  if someone books that seat, you cand find it by hash_id in redis.
#  redis helps you to set time expiration for that seat.
class TicketPurchaseListView(generics.ListCreateAPIView):
    queryset = TicketPurchase.objects.select_related('seat').all()
    serializer_class = TicketPurchaseSerializer
    permission_classes = (IsAuthenticated,)

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(TicketPurchaseListView, self).dispatch(*args, **kwargs)
