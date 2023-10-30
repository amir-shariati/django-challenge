from django.urls import path, include
from .views import (
    StadiumListView,
    MatchListView,
    SeatListView,
    TicketPurchaseListView
)

urlpatterns = [
    path("stadium/", StadiumListView.as_view(), name="stadium-list"),
    path("match/", MatchListView.as_view(), name="match-list"),
    path("seat/", SeatListView.as_view(), name="seat-list"),
    path("ticket/", TicketPurchaseListView.as_view(), name="ticket-list"),
]
