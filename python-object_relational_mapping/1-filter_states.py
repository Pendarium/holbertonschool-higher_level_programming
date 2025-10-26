#!/usr/bin/env python3
"""
Ce script liste tous les États dont le nom commence par 'N' (majuscule)
depuis la base de données MySQL `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Vérification rapide des arguments
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <utilisateur_mysql> <mot_de_passe_mysql> <nom_base>")
        sys.exit(1)

    utilisateur = sys.argv[1]
    mot_de_passe = sys.argv[2]
    base = sys.argv[3]

    # Connexion au serveur MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=utilisateur,
        passwd=mot_de_passe,
        db=base
    )

    # Création du curseur et exécution de la requête SQL
    curseur = db.cursor()
    # On récupère uniquement les lignes dont le nom commence par N et on garde la première occurrence de chaque nom
    curseur.execute(
        "SELECT id, name FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Récupération et affichage des résultats
    lignes = curseur.fetchall()
    noms_vus = set()
    for ligne in lignes:
        if ligne[1] not in noms_vus:
            print(ligne)
            noms_vus.add(ligne[1])

    # Fermeture du curseur et de la connexion
    curseur.close()
    db.close()
