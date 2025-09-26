class VerboseList(list):
    """
    A custom list class that prints a message
    whenever items are added or removed.

    Description:
        Classe personnalisée qui hérite de la liste Python standard.
        Elle affiche un message à chaque fois
        qu'un élément est ajouté (append, extend)
        ou retiré (remove, pop) de la liste.

    Methods:
        append(item): Add a single item to
        the list and print a confirmation message.
        extend(iterable): Add multiple items to the list and print the count.
        remove(item): Remove an item from the list and print a message.
        pop(index=-1): Remove and return an
        item at the given index and print a message.
    """

    def append(self, item):
        """Add an item to the end of the list and print a message.

        Description:
            Ajoute un élément à la fin de la
            liste et affiche un message de confirmation.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with the elements
        from the iterable and print a message.

        Description:
            Ajoute plusieurs éléments à la liste
            et affiche le nombre d'éléments ajoutés.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove the first occurrence of a value and print a message.

        Description:
            Supprime la première occurrence de
            l'élément spécifié et affiche un message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return the item at the given index and print a message.

        Description:
            Retire et retourne l'élément à
            l'index donné (ou le dernier par défaut),
            tout en affichant un message.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
