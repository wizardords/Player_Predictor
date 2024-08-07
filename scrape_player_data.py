import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_player_data():
    url = 'https://example.com/player-stats'  # Replace with actual URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Parse HTML to extract player data
    player_data = []
    for row in soup.find_all('tr'):  # Adjust based on actual HTML structure
        cols = row.find_all('td')
        if len(cols) > 0:
            player_data.append({
                'Name': cols[0].text.strip(),
                'Team': cols[1].text.strip(),
                'Points': int(cols[2].text.strip())
            })

    df = pd.DataFrame(player_data)
    df.to_csv('player_stats.csv', index=False)
    print('Data saved to player_stats.csv')

if __name__ == "__main__":
    scrape_player_data()
