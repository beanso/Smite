from django.db import models
from datetime import datetime, timedelta
from dateutil import parser

# Create your models here.

class Dicty(models.Model):
    name      = models.CharField(max_length=50)

class KeyVal(models.Model):
    container = models.ForeignKey(Dicty, db_index=True)
    key       = models.CharField(max_length=240, db_index=True)
    value     = models.CharField(max_length=240, db_index=True)

class Match(models.Model):
    mapid = models.IntegerField()
    queue = models.IntegerField()
    minutes = models.IntegerField()
import sys
from django.utils.timezone import utc
import pretty

class Player(models.Model):
    name = models.CharField(max_length=20)
    created = models.DateTimeField(null=True)
    last_login = models.DateTimeField(null=True)
    wins = models.IntegerField(null=True)
    losses = models.IntegerField(null=True)
    leaves = models.IntegerField(null=True)
    rank_confidence = models.FloatField(null=True)
    rank_stat = models.FloatField(null=True)
    level = models.IntegerField(null=True)
    updated = models.DateTimeField(auto_now=True)
    def updatelength(self):
        now = datetime.utcnow().replace(tzinfo=utc)
        length = now - self.updated
        return pretty.date(self.updated)



class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    secondary_description = models.CharField(max_length=255)
    item_id = models.IntegerField()
    menu_items = models.OneToOneField(Dicty)

class MatchDetails(models.Model):
    match = models.ForeignKey(Match)
    player_name = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    reference_name = models.CharField(max_length=25)
    win_status = models.CharField(max_length=15)
    entry_datetime = models.DateTimeField()
    damage_bot = models.IntegerField()
    damage_player = models.IntegerField()
    damage_done_magical = models.IntegerField()
    damage_done_physical = models.IntegerField()
    damage_taken = models.IntegerField()
    kills_player = models.IntegerField()
    deaths = models.SmallIntegerField()
    assists = models.SmallIntegerField()
    kills_bot = models.SmallIntegerField()
    final_match_level = models.SmallIntegerField()
    gold_earned = models.IntegerField()
    gold_per_minute = models.IntegerField()
    item_active_1 = models.ForeignKey(Item, related_name="active1")
    item_active_2 = models.ForeignKey(Item, related_name="active2")
    item_active_3 = models.ForeignKey(Item, related_name="active3")
    item_purch_1 = models.ForeignKey(Item, related_name="purch1")
    item_purch_2 = models.ForeignKey(Item, related_name="purch2")
    item_purch_3 = models.ForeignKey(Item, related_name="purch3")
    item_purch_4 = models.ForeignKey(Item, related_name="purch4")
    item_purch_5 = models.ForeignKey(Item, related_name="purch5")
    item_purch_6 = models.ForeignKey(Item, related_name="purch6")

class MatchSummary(models.Model):
    active_1 = models.CharField(max_length=50, null=True)
    active_2 = models.CharField(max_length=50, null=True)
    active_3 = models.CharField(max_length=50, null=True)
    item_1 = models.CharField(max_length=50, null=True)
    item_2 = models.CharField(max_length=50, null=True)
    item_3 = models.CharField(max_length=50, null=True)
    item_4 = models.CharField(max_length=50, null=True)
    item_5 = models.CharField(max_length=50, null=True)
    item_6 = models.CharField(max_length=50, null=True)
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    gold = models.IntegerField()
    level = models.IntegerField()
    match = models.IntegerField()
    match_time = models.DateTimeField()
    minutes = models.IntegerField()
    queue = models.CharField(max_length=25)
    win_status = models.CharField(max_length=5)
    player = models.ForeignKey(Player)
    god = models.CharField(max_length=25)


