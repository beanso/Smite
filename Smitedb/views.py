# Create your views here.
from django.template import Context, loader
from Smitedb.models import Player, MatchSummary
from django.http import HttpResponse
from django.shortcuts import render_to_response

def top_rated(request):
    player_sort_ranked = Player.objects.all().order_by("-rank_stat")
    return render_to_response('top_rated.html', {'player_sort_ranked': player_sort_ranked})

def player(request):
    player_dict = Player.objects.get(name=request.GET["name"])
    match_history = MatchSummary.objects.all().filter(player_id=player_dict.id).order_by("-match_time")
    return render_to_response('player.html', {"player": player_dict,
                                              "matches": match_history})