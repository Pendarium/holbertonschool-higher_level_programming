#!/usr/bin/python3
"""
Affiche toutes les lignes de la table states dont le nom correspond
exactement à l'argument passé, en utilisant .format() après échappement.
Usage: ./script.py <mysql_user> <mysql_password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == '__main__':
    utilisateur = sys.argv[1]
    mot_de_passe = sys.argv[2]
    base = sys.argv[3]
    etat_recherche = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=utilisateur,
        passwd=mot_de_passe,
        db=base
    )

    curseur = db.cursor()

    # Échapper la valeur utilisateur avant d'utiliser .format()
    # escape_string prend des bytes et renvoie des bytes
    escaped_bytes = MySQLdb.escape_string(etat_recherche.encode('utf-8'))
    escaped = escaped_bytes.decode('utf-8')

    # Construire la requête avec .format() (la valeur est déjà échappée)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(escaped)

    # Exécuter la requête (une seule execute() comme demandé)
    curseur.execute(query)

    # Afficher les résultats
    for ligne in curseur.fetchall():
        print(ligne)

    curseur.close()
    db.close()
