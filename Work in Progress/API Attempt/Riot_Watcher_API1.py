# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:27:51 2022

@author: Preston Robertson
"""

#%% Importing Libraries

from riotwatcher import LolWatcher, ApiError
import os
import json
import pandas as pd


#%% DELETE THIS

path = r"C://Users//Preston Robertson//OneDrive - Mississippi State University//Documents//Graduate//League Of Legends//Work in Progress//API Attempt//"


#%% Get API

def getAPI_key():
    f = open(path + "api_key.txt", "r")
    return f.read()



#%% Gathering Game List

data_temp = open(path + 'matchlist_na1_9-8.json')

Match_List = json.load(data_temp)




#%% Test with Dragon

lol_watcher = LolWatcher(getAPI_key())
my_region = 'na1'

me = lol_watcher.summoner.by_name(my_region, 'Leogi')
me_items = me.items()
me_list = list(me_items)
me_df = pd.DataFrame(me_list)
me_df.head(7)


my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])

# fetch last match detail
last_match = my_matches[0]
match_detail = lol_watcher.match.by_id(my_region, match_id= last_match)



#%% To Record

desired_list = ['assists',
                'baronKills',
                
                #'basicPings',
                # Some games just do not collect them
                
                'bountyLevel',
                'champExperience',
                'champLevel',
                'championName',
                'damageDealtToObjectives',
                'damageSelfMitigated',
                'deaths',
                'dragonKills',
                'firstBloodAssist',
                'firstBloodKill',
                'gameEndedInSurrender',
                'goldEarned',
                'goldSpent',
                'individualPosition',
                'inhibitorKills',
                'inhibitorsLost',
                'item0',
                'item1',
                'item2',
                'item3',
                'item4',
                'item5',
                'item6',
                'kills',
                'lane',
                'largestCriticalStrike',
                'largestKillingSpree',
                'longestTimeSpentLiving',
                'magicDamageDealtToChampions',
                'magicDamageTaken',
                'nexusLost',
                'objectivesStolen',
                'physicalDamageDealtToChampions',
                'physicalDamageTaken',
                'spell1Casts',
                'spell2Casts',
                'spell3Casts',
                'spell4Casts',
                'summoner1Casts',
                'summoner1Id',
                'summoner2Casts',
                'summoner2Id',
                'summonerId',
                'teamEarlySurrendered',
                'teamId',
                'timeCCingOthers',
                'timePlayed',
                'totalDamageDealtToChampions',
                'totalDamageShieldedOnTeammates',
                'totalDamageTaken',
                'totalHeal',
                'totalHealsOnTeammates',
                'totalMinionsKilled',
                'totalTimeCCDealt',
                'totalTimeSpentDead',
                'trueDamageDealtToChampions',
                'trueDamageTaken',
                'turretTakedowns',
                'turretsLost',
                'visionScore',
                'visionWardsBoughtInGame',
                'wardsKilled',
                'wardsPlaced',
                'win']


#%% Test before Main




my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])



# fetch last match detail
last_match = my_matches[0]
match_detail = lol_watcher.match.by_id(my_region, match_id= last_match)
current_mode = match_detail['info']['gameMode']






participants_row = {}
# Clearing repeatable dictionary

for i in range(0, len(desired_list)):
# Looping to gather all information from the desired list    
    
    participants_row[desired_list[i]] = match_detail['info']['participants'][0][desired_list[i]]
    # Gathering all data from desired list
    
    participants_row['GameID'] = last_match
    # Recording GameID
    
    participants_row['GameMode'] = current_mode
    # Recording GameMode
    
games_info = pd.DataFrame.from_dict(participants_row, orient = 'index')
# Turning the Dictionary to Dataframe

games_info = games_info.T
# Translating the Features to the columns




#%% Main




import time
start_time = time.time()






def GetDesiredListData(n):
    start_time = time.time()
    my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])
    
    
    
    # fetch last match detail
    last_match = my_matches[0]
    match_detail = lol_watcher.match.by_id(my_region, match_id= last_match)
    current_mode = match_detail['info']['gameMode']
    
    
    
    
    
    
    participants_row = {}
    # Clearing repeatable dictionary
    
    for i in range(0, len(desired_list)):
    # Looping to gather all information from the desired list    
        
        participants_row[desired_list[i]] = match_detail['info']['participants'][0][desired_list[i]]
        # Gathering all data from desired list
        
        participants_row['GameID'] = last_match
        # Recording GameID
        
        participants_row['GameMode'] = current_mode
        # Recording GameMode
        
    games_info = pd.DataFrame.from_dict(participants_row, orient = 'index')
    # Turning the Dictionary to Dataframe
    
    games_info = games_info.T
    # Translating the Features to the columns
    
    
    # for z in range(0,len(Match_List)):
        
        
        
        
        
        
        # Turn on if you want all the data from the random game list
        # Roughly 10,000 games per.
        
    for z in range(0,n):
        
        match_detail = lol_watcher.match.by_id(my_region, match_id= "NA1_" + str(Match_List[z]))
        current_mode = match_detail['info']['gameMode']
        current_match = Match_List[z]
        
        
        for j in range(0, len(match_detail['info']['participants'])):
            
            participants_row = {}
            # Clearing repeatable dictionary
            
            for i in range(0,len(desired_list)):
                
                participants_row[desired_list[i]] = match_detail['info']['participants'][j][desired_list[i]]
                # Gathering all data from desired list
                
                participants_row['GameID'] = current_match
                # Recording GameID
                
                participants_row['GameMode'] = current_mode
                # Recording GameMode
            
                
            # Back to j For Loop
            temp_df = pd.DataFrame.from_dict(participants_row, orient = 'index')
            # Turning the Dictionary to Dataframe
            
            temp_df = temp_df.T
            # Translating the Features to the columns
            
            games_info = pd.concat([games_info,temp_df])
            # Adding newly recorded values to the dataframe
        
        print(z)
        
    print('---%s seconds ---' % (time.time() - start_time))    
    return(games_info)
    
    
print('---%s seconds ---' % (time.time() - start_time))




#%%


