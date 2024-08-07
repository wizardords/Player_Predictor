import requests
import pandas as pd

API_KEY = '5t6LdJbGKKag8w3CCaeib9gKHGXXzHtE6r7Z1ufm'
BASE_URL = 'https://api.sportradar.com/soccer-t3/eu/en/players/{player_id}/profile.json?api_key={api_key}'

def get_player_data(player_id):
    url = BASE_URL.format(player_id=player_id, api_key=API_KEY)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

player_ids = ['player_id1', 'player_id2', 'player_id3']
player_data = [get_player_data(player_id) for player_id in player_ids]

df = pd.json_normalize(player_data)
df.to_csv('player_data.csv', index=False)
