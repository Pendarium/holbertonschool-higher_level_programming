import requests
import csv


def fetch_and_print_posts():
    """
    Récupère une liste de publications depuis l'API JSONPlaceholder
    et affiche les titres de chaque publication dans la console.

    Étapes :
    1. Envoie une requête HTTP GET à l'URL
    de l'API (https://jsonplaceholder.typicode.com/posts).
    2. Vérifie que la réponse est valide (code 200).
    3. Convertit la réponse JSON en liste de dictionnaires Python.
    4. Parcourt chaque publication et affiche uniquement le titre.

    Aucune donnée n'est enregistrée
    localement : cette fonction sert à consulter.
    """
    # Envoi d'une requête GET à l'API
    # JSONPlaceholder pour obtenir la liste des posts
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Vérification du code de statut HTTP
    # pour s'assurer que la requête a réussi
    if response.status_code != 200:
        print("Erreur ! Statut :", response.status_code)
        return

    # Si tout va bien, affichage du code de statut
    print("Status Code:", response.status_code)

    # Conversion du contenu JSON reçu en
    # structure Python (liste de dictionnaires)
    data = response.json()

    # Parcours de la liste et affichage du titre de chaque post
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    """
    Récupère une liste de publications depuis l'API JSONPlaceholder
    et enregistre certaines informations
    dans un fichier CSV local nommé 'posts.csv'.

    Étapes :
    1. Envoie une requête HTTP GET à l'API
    (https://jsonplaceholder.typicode.com/posts).
    2. Vérifie que la réponse est valide (code 200).
    3. Extrait les champs 'id', 'title' et 'body' de chaque publication.
    4. Crée un fichier CSV avec ces informations.
    5. Écrit les données dans le fichier ligne par ligne.
    6. Informe l’utilisateur que le fichier a bien été généré.

    Ce fichier CSV peut ensuite être ouvert
    dans Excel, LibreOffice ou tout autre tableur.
    """
    # Envoi d'une requête GET pour récupérer les posts depuis l'API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Vérifie que la réponse est correcte
    if response.status_code != 200:
        print("Erreur ! Statut :", response.status_code)
        return

    # Conversion du JSON en structure Python
    data = response.json()

    # Création d'une liste de dictionnaires avec uniquement les champs utiles
    posts_to_csv = []
    for post in data:
        posts_to_csv.append({
            "id": post["id"],      # Identifiant unique du post
            "title": post["title"],  # Titre du post
            "body": post["body"]     # Contenu du post
        })

    # Ouverture (ou création) d'un fichier CSV en mode écriture
    # newline="" évite d’insérer des lignes
    # vides entre chaque enregistrement sur Windows
    # encoding="utf-8" garantit une compatibilité avec les caractères accentués
    with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "title", "body"]  # Noms des colonnes dans le CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Écrit l’en-tête (les noms de colonnes)
        writer.writeheader()

        # Écrit chaque ligne correspondant à un post
        for post in posts_to_csv:
            writer.writerow(post)

    # Confirmation dans la console
    print("Les données ont été exportées dans 'posts.csv'")
