import sys
import requests

def check_website_status():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python check_website.py <URL>")
    
    url = sys.argv[1]

    try:
        response = requests.get(url)
        print(f"Website {url} is {'working' if response.status_code == 200 else f'not working (Status: {response.status_code})'}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

if __name__ == "__main__":
    try:
        check_website_status()
    except ValueError as e:
        print(e)
