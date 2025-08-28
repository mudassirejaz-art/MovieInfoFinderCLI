import requests

API_KEY = "bc9708f3"  # no leading/trailing spaces 
BASE_URL = "http://www.omdbapi.com/"

def fetch_movie(title):
    params = {"t": title, "apikey": API_KEY}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "False":
            return None, data.get("Error")
        return data, None
    except Exception as e:
        return None, str(e)
