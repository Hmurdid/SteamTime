from API.CustomRequest import SteamRequest

info = SteamRequest('E42B53F855437905C3D239ED4AFB5BC2', '76561198836194029')
print(info)

response_player, response_games_data = info
print(response_player.json())
print(f"\n\n\n")
print(response_games_data.json())
