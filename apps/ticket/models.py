import hashlib
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Stadium(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Stadium name'))
    location = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')


class Match(models.Model):
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    date_time = models.DateTimeField(verbose_name='Match time')
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    @property
    def match_title(self):
        return f'{self.stadium}, {self.team1}-{self.team2}, {self.date_time}'

    def __str__(self):
        return f'{self.stadium}, {self.team1}-{self.team2}, {self.date_time}'

    class Meta:
        verbose_name = _('Match')
        verbose_name_plural = _('Matches')


class Seat(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    row = models.IntegerField()
    number = models.IntegerField()
    seat_match_hash_id = models.CharField(max_length=64, unique=True, default=None, editable=False)

    @property
    def seat_title(self):
        return f'{self.match}, row:{self.row}, number:{self.number}'

    def save(self, *args, **kwargs):
        if self.seat_match_hash_id is None:
            m = hashlib.sha256()
            byte_match = str(self.match).encode()
            m.update(byte_match)
            # converting to string
            str_row = str(self.row)
            str_number = str(self.number)
            # converting string to bytes
            byte_row = str_row.encode()
            byte_number = str_number.encode()
            m.update(byte_row)
            m.update(byte_number)
            self.seat_match_hash_id = m.hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.match}, row:{self.row}, number:{self.number}'

    class Meta:
        verbose_name = _('Seat')
        verbose_name_plural = _('Seats')


class TicketPurchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.user}, {self.ticket_id}, {self.timestamp}'

    class Meta:
        verbose_name = _('Ticket Purchase')
        verbose_name_plural = _('Ticket Purchases')
