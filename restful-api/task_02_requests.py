import requests
import csv

requests.get("https://jsonplaceholder.typicode.com/posts")
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code != 200:
    print("Status Code:", response.status_code)
else:
    print("Status Code:", response.status_code)

data = response.json()
for post in data:
    print(post["title"])

posts_to_csv = []
for post in data:
    posts_to_csv.append({"id": post["id"],
                         "title": post["title"],
                         "body": post["body"]})
with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id", "title", "body"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for post in posts_to_csv:
        writer.writerow(post)

    print("Les données ont été exportées dans 'posts.csv'")
