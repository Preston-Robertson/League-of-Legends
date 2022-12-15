# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:27:51 2022

@author: Preston Robertson
"""

#%% Importing Libraries

from riotwatcher import LolWatcher
import pandas as pd
import urllib.request, json, time, os
from tqdm import tqdm
from datetime import date, timedelta


#%% Main


Summoner_Name = 'DoubleLift'
my_region = 'na1'



# Functions


## GetDesiredListData(n)
### Makes a pandas data frame of desired data points.

## GetCSVofDesiredList(n)
### Makes a CSV file of above code.



# Notes

# Rate Limits
## 20 requests every 1 seconds(s)
## 100 requests every 2 minutes(s)


# Use link below to get API key
## https://developer.riotgames.com/



#%% Setting Desired List



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




#%% Get API

def getAPI_key():
    f = open(path + "\\api_key.txt", "r")
    return f.read()



#%% Gathering Game List

def GetJSONdata():
    staticURL = 'https://canisback.com/matchId/matchlist_na1.json'
    # Only change URL if the there was an update to the website
    
    with urllib.request.urlopen(staticURL) as url:
        Match_List = json.load(url)
        #print(Match_List[0])
        
    current_json = date.today().strftime("%b-%d-%Y")
    #print(current_json)
    # Setting the date
    
    return(Match_List)



#%% Pre-Lim Code to Functions


# Loading Neccessary Data
path = os.getcwd()
lol_watcher = LolWatcher(getAPI_key())
current_json = date.today().strftime("%b-%d-%Y")
rate_limit = 0.833333 
# Rate limit is (iteration/second)



# Test
me = lol_watcher.summoner.by_name(my_region, Summoner_Name)
if me['name'] == Summoner_Name:
    print('API Connected')

  



#%% Pulling from API






def GetDesiredListData(n):
    # where "n" is the the number of games you want to extract
    
    start_time = time.time()
    
    
    Match_List = GetJSONdata()
    # Getting Match_List from website
    
    
    
    completion_time_s = round(n/rate_limit, 1)
    # Estimating completion time and rounding the seconds to the tenth
    
    cp_time_m = str(timedelta(seconds=completion_time_s))
    cp_time_l = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()+completion_time_s)))
    
    print('Estimated time until completion:\n {}'.format(cp_time_m))
    print('Completion at local time:\n {}'.format(cp_time_l))
    
    
    me = lol_watcher.summoner.by_name(my_region, 'DoubleLift')
    my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])
    last_match = my_matches[0]
    match_detail = lol_watcher.match.by_id(my_region, match_id= last_match)
    current_mode = match_detail['info']['gameMode']
    # Setting up first column and testing
    
    
    
    
    
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
        
    for z in tqdm(range(0,n),  ncols=100):
        
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
        
        #print(z / n)
        
    
    print('\n---%s seconds ---' % (time.time() - start_time))    
    return(games_info)
    




#%% Making CSV file


def GetCSVofDesiredList(n):
    # Where "n" is the amount of games extracted
    
    games_info = GetDesiredListData(n)
    # Get the data
    
    matches = str(n)
    
    if os.path.exists(path+ '/' + current_json):
    # If folder for today exists then print to folder
        
        games_info.to_csv(path + '/' + current_json + '/' + current_json + '_' + matches +'matches' + '.csv')
        # Collected data 
        
        print('.CSV file made')
        
    else: 
        new_path = os.path.join(path, current_json)
        # Creating folder for today's date
        
        print("Directory '% s' created" % current_json)
        
        try: 
            os.mkdir(new_path) 
            # Trying to make the folder in the new path
            
        except OSError as error: 
            print(error) 
            
        games_info.to_csv(path + '/' + current_json + '/' + current_json + '_' + matches +'matches' + '.csv')
        # Collected data 
            
        


