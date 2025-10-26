#!/usr/bin/env python3

"""
Liste tous les états dont le nom commence par 'N' (majuscule)
depuis la base de données hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Récupération des arguments
    utilisateur = sys.argv[1]
    mot_de_passe = sys.argv[2]
    base = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=utilisateur,
        passwd=mot_de_passe,
        db=base
    )

    # Création du curseur et exécution de la requête SQL
    curseur = db.cursor()
    curseur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Affichage des résultats
    for ligne in curseur.fetchall():
        print(ligne)

    # Fermeture du curseur et de la connexion
    curseur.close()
    db.close()
