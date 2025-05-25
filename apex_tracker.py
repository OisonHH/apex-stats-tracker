import requests

API_KEY = "2c3277b8-5da7-4796-a95d-a6cc5f61b194"
BASE_URL = "https://public-api.tracker.gg/v2/apex/standard/profile/origin/"

def get_apex_stats(username):
    url = BASE_URL + username
    headers = {
        "TRN-Api-Key": API_KEY,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"  
    }
    response = requests.get(url, headers=headers)
    print("Statuskod:", response.status_code)
    print("Responsens innehåll:", response.text)
    
    if response.status_code == 200:
        data = response.json()
        try:
            stats = data['data']['segments'][0]['stats']
            kills = stats['kills']['value']
            level = stats['level']['value']
            print(f"Spelare: {username}")
            print(f"Level: {level}")
            print(f"Totala kills: {kills}")
        except KeyError:
            print("Kunde inte hitta statistik för spelaren.")
    else:
        print(f"Fel vid hämtning av data: Statuskod {response.status_code}")

if __name__ == "__main__":
    user = input("Ange Apex Origin-användarnamn: ")
    get_apex_stats(user)
