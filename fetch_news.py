import requests
from config import API_KEY

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error:", response.status_code)
        return []
    
    return response.json()