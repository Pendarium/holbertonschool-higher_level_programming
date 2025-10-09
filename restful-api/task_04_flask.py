from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire des utilisateurs (vide au démarrage)
users = {}

@app.route("/")
def home():
    """Racine de l'API - Retourne un message de bienvenue"""
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    """Vérifie le statut de l'API"""
    return "OK"

@app.route("/data")
def get_data():
    """Retourne la liste des noms d'utilisateurs disponibles"""
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    """Retourne les informations complètes d'un utilisateur donné"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """Ajoute un nouvel utilisateur via une requête POST"""
    data = request.get_json()

    # Vérifie si les données sont présentes
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    # Vérifie la présence du champ "username"
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Ajoute l'utilisateur dans le dictionnaire
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    # Démarrage du serveur Flask sur le port 5000
    app.run(port=5000)
