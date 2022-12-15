# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:05:53 2022

@author: Preston Robertson
"""

#%% Importing Libraries

from riotwatcher import LolWatcher, ApiError
import cassiopeia as cass
import requests
import ujson
import os
import pandas as pd


#%% Get API

def getAPI_key():
    f = open("C:/Users/Preston Robertson/OneDrive - Mississippi State University/Documents/Graduate/League Of Legends/Work in Progress/API Attempt/api_key.txt", "r")
    return f.read()

cass.set_riot_api_key(getAPI_key())

#%% Defining Parameters

# Defning Server
cass.Settings()


#%% Test with Dragon

lol_watcher = LolWatcher(getAPI_key())
my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'Leogi')
me_items = me.items()
me_list = list(me_items)
me_df = pd.DataFrame(me_list)
me_df.head(7)



#%% Test

from cassiopeia import Summoner

me = Summoner(name="Leogi", region ="NA")
good_with = me.champion_masteries.filter(lambda cm: cm.level >= 6)
print([cm.champion.name for cm in good_with])


match = me.match_history[0]
champion_played = match.participants[me].champion


#%% Defining

def getChallengerPlayers():
    challenger_league = cass.get_challenger_league(queue = cass.Queue.ranked_solo_fives, region = "NA")
    
    
    summoner = challenger_league[0].summoner
    match_history = summoner.match_history(queue = {cass.Queue.ranked_solo_fives},
                                           begin_index = 0,
                                           end_index = 4)
    
    for match in match_history:
        print(match.duration)
        match.kills_heatmap()
    
    
    
#%%

getChallengerPlayers()























