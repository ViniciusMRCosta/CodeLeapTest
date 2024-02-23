import views
import requests

def test_create_post():
    data = {
        "username": "teste username",
        "title": "teste post title",
        "content": "teste post content"
    }
    response = views.create_post(data)
    
def test_get_posts():
    response = views.get_posts()

def test_update_post():
    item_id = 67591
    data = {
        "title": "Updated post title again",
        "content": "Updated post content again"
    }
    response = views.update_post(item_id, data)

def test_delete_post():
    item_id = 67591
    response = views.delete_post(item_id)

def main_menu():
    while True:
        print("1. Create Post")
        print("2. Get Posts")
        print("3. Update Post")
        print("4. Delete Post")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            test_create_post()
        elif choice == "2":
            test_get_posts()
        elif choice == "3":
            test_update_post()
        elif choice == "4":
            test_delete_post()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()
