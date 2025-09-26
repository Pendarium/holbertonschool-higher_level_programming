#!/usr/bin/env python3


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been iterated over.

    Description:
        Cette classe prend un itérable en entrée et agit comme un itérateur.
        Elle suit combien d’éléments ont été
        parcourus jusqu’à présent via la méthode get_count().

    Attributes:
        iterator (iterator): L’itérateur interne dérivé de l’itérable donné.
        count (int): Le compteur du nombre d’éléments itérés.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Description:
            Initialise un itérateur interne et met le compteur à zéro.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself.

        Description:
            Retourne l'objet lui-même pour permettre 
            l'utilisation dans une boucle for.
        """
        return self

    def __next__(self):
        """
        Return the next item and increment the count.

        Description:
            Retourne l’élément suivant de l’itérateur
            tout en incrémentant le compteur.
            Lève StopIteration s’il n’y a plus d’éléments.
        """
        item = next(self.iterator)  # May raise StopIteration, as required
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated.

        Description:
            Retourne le nombre total d’éléments
            récupérés jusqu’à maintenant.
        """
        return self.count
