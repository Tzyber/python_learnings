from multipledispatch import dispatch

class calculator:
    """
    Ein einfacher Rechner, der `multipledispatch` nutzt, um Methoden basierend auf
    zwei Argumenttypen zu überladen.
    """
    @dispatch(int, int)
    def add(self, a, b):
        """
        Addiert zwei ganze Zahlen.
        """
        return a + b

    @dispatch(float, float)
    def add(self, a, b):
        """
        Addiert zwei Fließkommazahlen.
        """
        return a + b

    @dispatch(str, str)
    def add(self, a, b):
        """
        Verkettet zwei Strings.
        """
        return a + b

calc = calculator()
print(calc.add(3, 5))          # Ausgabe: 8
print(calc.add(3.14, 2.71))   # Ausgabe: 5.85
print(calc.add("Hello, ", "World!"))  # Ausgabe: Hello,