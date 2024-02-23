import requests

item_id = 67591

data = {
    "title": "Updated post title",
    "content": "Updated post content"
}

response = requests.patch(f"https://dev.codeleap.co.uk/careers/{item_id}/", json=data)

if response.status_code == 200:
    print("Post updated successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
