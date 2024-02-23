import requests

item_id = 67592

response = requests.delete(f"https://dev.codeleap.co.uk/careers/{item_id}/")

if response.status_code == 204:
    print("Post deleted successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
