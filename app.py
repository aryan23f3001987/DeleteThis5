import requests

url = "https://api.github.com/search/users"
params = {
    "q": "location:Mumbai followers:>140",
    "sort": "joined",
    "order": "desc",
    "per_page": 1
}
headers = {"Accept": "application/vnd.github.v3+json"}

response = requests.get(url, params=params, headers=headers)
data = response.json()

if data.get("items"):
    user = data["items"][0]
    # Fetch full user profile for created_at
    profile = requests.get(user["url"], headers=headers).json()
    print(profile["created_at"])
else:
    print("No matching user found.")
