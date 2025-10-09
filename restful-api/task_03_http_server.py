from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Définition d'une classe qui gère les requêtes HTTP


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Classe de gestion des requêtes HTTP pour une API simple.
    Elle redéfinit la méthode do_GET() pour gérer différents endpoints :
    - /         → renvoie un message texte simple
    - /data     → renvoie un jeu de données JSON
    - /status   → renvoie "OK" pour vérifier le statut du serveur
    - autres    → renvoie une erreur 404
    """

    def do_GET(self):
        """Gère les requêtes HTTP GET envoyées au serveur."""

        # Récupère le chemin de la requête (ex: '/', '/data', '/status', etc.)
        path = self.path

        # Endpoint racine "/"
        if path == "/":
            self.send_response(200)  # Code de succès HTTP 200 (OK)
            self.send_header("Content-Type", "text/plain")
            # Type de contenu texte brut
            self.end_headers()  # Fin des en-têtes
            self.wfile.write(b"Hello, this is a simple API!")
            # Réponse envoyée au client

        # Endpoint "/data" → renvoie un JSON
        elif path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data).encode("utf-8")
            # Conversion en texte JSON (bytes)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)

        # Endpoint "/status" → renvoie "OK"
        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Endpoint "/info" → renvoie des informations sur l'API
        elif path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            response = json.dumps(info).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response)

        # Si le chemin ne correspond à aucun endpoint connu → erreur 404
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


# Point d'entrée principal du programme
if __name__ == "__main__":
    # Création d'un serveur HTTP écoutant sur le port 8000
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)

    print("🚀 Serveur en cours d'exécution sur http://localhost:8000")
    try:
        # Boucle principale : le serveur attend les requêtes en continu
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du serveur.")
        httpd.server_close()
