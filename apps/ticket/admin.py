from django.contrib import admin
from .models import Stadium, Match, Seat, TicketPurchase


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 25


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'stadium', 'date_time')
    search_fields = ('match_title',)
    autocomplete_fields = ('stadium',)
    list_per_page = 25


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('match', 'seat_match_hash_id', 'row', 'number')
    search_fields = ('seat_title',)
    autocomplete_fields = ('match',)
    readonly_fields = ('seat_match_hash_id',)
    list_per_page = 25


@admin.register(TicketPurchase)
class TicketPurchaseAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'seat', 'timestamp', 'timestamp')
    autocomplete_fields = ('user', 'seat')
    list_per_page = 25
