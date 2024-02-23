import requests

data = {
    "username": "teste username",
    "title": "teste post title",
    "content": "teste post content"
}
try:
    response = requests.post(r"https://dev.codeleap.co.uk/careers/", json=data)
    if response.status_code == 200:
        print("Post created successfully!")
        print(f"ID: {response.json()['id']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except Exception as e:
    print(f"Erro: {e}")
    exit()
