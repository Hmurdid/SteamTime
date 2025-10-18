import requests

#Function to return result into main.py
def getSteamTime(STEAM_API_KEY, STEAM_ID):
    
    if not STEAM_API_KEY or not STEAM_ID:
        return {
            'success': False,
            'error': 'API key or Steam ID is empty'
        }
    
    
    #Get users nickname & return fail if success == false
    url_user = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params_user = {
        'key': STEAM_API_KEY,
        'steamids': STEAM_ID
    }
    
    response_user = requests.get(url_user, params=params_user)
    if response_user.status_code != 200:
        return {'success': False, 'error': f'Failed request: {response_user.status_code}'}
        
    user_data = response_user.json()
    if 'response' not in user_data or 'players' not in user_data['response'] or not user_data['response']['players']:
        return {'success': False, 'error': 'Invalid Steam ID or private profile'}

    nickname = user_data['response']['players'][0].get('personaname', 'Unknown')


    #Get list of all games
    url_games = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    params_games = {
        'key': STEAM_API_KEY,
        'steamid': STEAM_ID,
        'include_appinfo': True,
        'include_played_free_games': True,
        'format': 'json'
    }
    
    
    response_games = requests.get(url_games, params=params_games)
    if response_games.status_code != 200:
        return {'success': False, 'error': f'Failed request for games: {response_games.status_code}'}

    data = response_games.json()
    if 'response' not in data:
        return {'success': False, 'error': 'Invalid API key or failed request for games'}
    
    games = data['response'].get('games', [])
    if not games:
         return {
            'success': False,
            'error': 'No games found or profile is private'
            }
    #Sort games by time
    games_sorted = sorted(games, key=lambda x: x['playtime_forever'], reverse=True)
    
    #*
    
    #Forming text
    result_text = f"Games of the user {nickname}:\n\n"
    for game in games_sorted:
        hours = round(game['playtime_forever'] / 60)
        result_text += f"{game['name']:<50} {hours:>8} hrs\n"


    #Sending text
    return {
        'success': True,
        'nickname': nickname,
        'total_games': len(games),
        'games_list_text': result_text,  #Final text to show
        'games': games_sorted  #If u need to process data
    }
