#!/usr/bin/env python3


class Fish:
    """
    Base class representing a fish.

    Description:
        Classe de base représentant un poisson, avec des comportements
        typiques comme nager et définir son habitat naturel.
    """

    def swim(self):
        """
        Make the fish swim.

        Description:
            Affiche un message indiquant que le poisson nage.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Describe the fish's habitat.

        Description:
            Affiche un message indiquant que le poisson vit dans l’eau.
        """
        print("The fish lives in water")


class Bird:
    """
    Base class representing a bird.

    Description:
        Classe de base représentant un oiseau, avec la capacité de voler
        et une indication de son habitat naturel.
    """

    def fly(self):
        """
        Make the bird fly.

        Description:
            Affiche un message indiquant que l’oiseau vole.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Describe the bird's habitat.

        Description:
            Affiche un message indiquant que l’oiseau vit dans le ciel.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish,
    combining features of both fish and birds.

    Description:
        Classe représentant un poisson volant, héritant à la fois des
        comportements des poissons et des oiseaux. Elle redéfinit les méthodes
        pour refléter son caractère hybride.
    """

    def fly(self):
        """
        Make the flying fish fly.

        Description:
            Affiche un message indiquant que le poisson volant plane dans les
            airs.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Make the flying fish swim.

        Description:
            Affiche un message indiquant que le poisson volant nage.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Describe the flying fish's habitat.

        Description:
            Affiche un message indiquant que le poisson volant vit à la fois
            dans l’eau et dans le ciel.
        """
        print("The flying fish lives both in water and the sky!")
