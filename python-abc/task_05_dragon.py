#!/usr/bin/env python3


class SwimMixin:
    """
    Mixin class providing swimming ability.

    Description:
        Ce mixin ajoute la capacité de nager aux classes qui l'héritent.
    """

    def swim(self):
        """
        Make the creature swim.

        Description:
            Affiche un message indiquant que la créature nage.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing flying ability.

    Description:
        Ce mixin ajoute la capacité de voler aux classes qui l'héritent.
    """

    def fly(self):
        """
        Make the creature fly.

        Description:
            Affiche un message indiquant que la créature vole.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon that can both swim and fly.

    Description:
        Le dragon hérite des mixins SwimMixin et FlyMixin, ce qui lui
        permet de nager et de voler. Peut aussi rugir.
    """

    def roar(self):
        """
        Make the dragon roar.

        Description:
            Affiche un message indiquant que le dragon rugit.
        """
        print("The dragon roars!")