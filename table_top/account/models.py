from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    discord = models.CharField(max_length=50)
    platform_played_on = models.CharField(max_length=200)
    game_systems_looking_for = models.CharField(max_length=255)
    campaign_length = models.CharField(max_length=255)
    player = models.CharField(max_length=200)
    gm = models.CharField(max_length=200)
    looking_for_game = models.CharField(max_length=200) 
    party_leaders =  models.CharField(max_length=200) 
    chat_name =  models.CharField(max_length=200) 
    rating = models.CharField(max_length=200)
    lvl_of_rp = models.CharField(max_length=200)