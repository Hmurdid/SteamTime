import requests
from Core.validations import Steam

def SteamRequest(STEAM_API_KEY, STEAM_ID):
    
    Steam.validateInput(STEAM_API_KEY, STEAM_ID)    
    
    # Server which gives info about player & his games
    url_player = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/'
    url_games_data = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
    
    # Paraneters to requests
    params_player = {
        'key': STEAM_API_KEY,
        'steamids': STEAM_ID
    }
    params_data = {
        'key': STEAM_API_KEY,
        'steamid': STEAM_ID,
        'include_appinfo': True,
        'include_played_free_games': True,
        'format': 'json'
    } 
    
    response_player = requests.get(url_player, params=params_player)
    response_games_data = requests.get(url_games_data, params=params_data)
    
    player_data = Steam.validateApiResponse(response_player, 'player')
    Steam.validateUserData(player_data)
    
    games_data = Steam.validateApiResponse(response_games_data, 'games')
    Steam.validateGamesData(games_data)
    
    return response_player, response_games_data
