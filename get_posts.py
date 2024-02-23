import requests

response = requests.get(r"https://dev.codeleap.co.uk/careers/")

if response.status_code == 200:
    posts = response.json()
    print(type(posts))
    print(posts)
    print("Posts:")
    for post in posts['results']:
        print(f"- ID: {post['id']}, Username: {post['username']}, Title: {post['title']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
