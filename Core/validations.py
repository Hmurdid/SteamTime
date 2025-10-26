class Steam:
    
    @staticmethod
    def validateInput(steamapi, steamid):
        if not steamapi or len(steamapi) != 32:
            raise ValueError(f'Invalid API key')
            
        if not steamid or len(steamid) != 17:
            raise ValueError(f'Invalid ID key')
        if not steamid.isdigit():
            raise ValueError(f'ID must contain digits only')
    
    
    
    @staticmethod
    def validateApiResponse(response, entity_name='data'):
        if response.status_code != 200:
            raise ValueError(f'Failed to request: HTTP {response.status_code}')
        
        data = response.json()
        if 'response' not in data:
            raise ValueError(f'Invalid API response from {entity_name}')
        return data
        
    
    
    @staticmethod
    def validateUserData(data):
        if 'players' not in data['response'] or not data['response']['players']:
            raise ValueError('Invalid Steam ID or private profile')
        return data['response']['players'][0]
    
    
    
    
    def validateGamesData(data):
        games = data['response'].get('games', [])
        if not games:
            raise ValueError('No games found or profile is private')
        return games
