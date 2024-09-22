import requests

url = 'https://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Website is reachable!")
    else:
        print(f"Failed with status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
