from API.CustomRequest import SteamRequest

steapi = input('api: ')
steid = input('id: ')

info = SteamRequest(steapi, steid)
print(info)

response_player, response_games_data = info
print(response_player.json())
print(f"\n\n\n")
print(response_games_data.json())
