from functools import singledispatchmethod


class Rechner:
    """
    Eine Klasse zur Demonstration von Methodenüberladung mit `singledispatchmethod`.
    Unterschiedliche Datentypen werden unterschiedlich verarbeitet.
    """

    @singledispatchmethod #Dekoratoren
    def add(self, x):
        """
        Die Standard-Methode, die aufgerufen wird, wenn kein spezifischerer Typ passt.

        Args:
            x: Das Eingabeargument beliebigen Typs.
        """
        print("standart", x)

    @add.register
    def _(self, x: int):
        """
        Verarbeitung für ganze Zahlen (int): Addiert 10.
        """
        print("int", x + 10)

    @add.register
    def _(self, x: str):
        """
        Verarbeitung für Text (str): Hängt '!!!' an.
        """
        print("str", x + "!!!")

rechner = Rechner()
rechner.add(3.14)
rechner.add(5)
rechner.add("Hallo")
