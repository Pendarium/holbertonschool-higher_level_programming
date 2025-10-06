import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code != 200:
        print("Erreur ! Statut :", response.status_code)
        return
    print("Status Code:", response.status_code)
    data = response.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code != 200:
        print("Erreur ! Statut :", response.status_code)
        return
    data = response.json()
    posts_to_csv = []
    for post in data:
        posts_to_csv.append({
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        })
    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for post in posts_to_csv:
            writer.writerow(post)
    print("Les données ont été exportées dans 'posts.csv'")
