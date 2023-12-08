import math


class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Type of numerator and denominator of fraction must be integer!")
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def reduct(numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        return int(numerator / gcd), int(denominator / gcd)

    def __add__(self, summand):
        if not isinstance(summand, Fraction) and not isinstance(summand, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(summand, int):
            summand = Fraction(summand, 1)

        denominator = math.lcm(self.denominator, summand.denominator)
        numerator = int((self.numerator * denominator / self.denominator) + (summand.numerator * denominator / summand.denominator))
        numerator, denominator = Fraction.reduct(numerator, denominator)
        return Fraction(numerator, denominator)

    def __sub__(self, subtracted):
        if not isinstance(subtracted, Fraction) and not isinstance(subtracted, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(subtracted, int):
            subtracted = Fraction(subtracted, 1)

        denominator = math.lcm(self.denominator, subtracted.denominator)
        numerator = int((self.numerator * denominator / self.denominator) - (subtracted.numerator * denominator / subtracted.denominator))

        numerator, denominator = Fraction.reduct(numerator, denominator)
        return Fraction(numerator, denominator)

    def __mul__(self, multiplier):
        if not isinstance(multiplier, Fraction) and not isinstance(multiplier, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(multiplier, int):
            multiplier = Fraction(multiplier, 1)

        numerator = self.numerator * multiplier.numerator
        denominator = self.denominator * multiplier.denominator

        numerator, denominator = Fraction.reduct(numerator, denominator)
        return Fraction(numerator, denominator)

    def __truediv__(self, divisor):
        if not isinstance(divisor, Fraction) and not isinstance(divisor, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(divisor, int):
            divisor = Fraction(divisor, 1)

        numerator = self.numerator * divisor.denominator
        denominator = self.denominator * divisor.numerator

        numerator, denominator = Fraction.reduct(numerator, denominator)
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction) and not isinstance(other, int):
            raise ValueError("Wrong type of second argument!")
        if isinstance(other, int):
            other = Fraction(other, 1)
        numerator_1, denominator_1 = Fraction.reduct(self.numerator, self.denominator)
        numerator_2, denominator_2 = Fraction.reduct(other.numerator, other.denominator)
        return numerator_1 == numerator_2 and denominator_1 == denominator_2

    def is_bigger(self, other):
        denominator = math.lcm(self.denominator, other.denominator)
        numerator_1 = self.numerator * denominator / self.denominator
        numerator_2 = other.numerator * denominator / other.denominator
        return numerator_1 > numerator_2

    def __str__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print("1/2 + 1/4 =", x + y)
    print("1/2 + 5 = ", x + 5)

    print("1/2 - 1/4 =", x - y)
    print("1/2 - 7 =", x - 7)

    print("1/2 * 1/4 =", x * y)
    print("1/2 * 2 =", x * 2) 

    print("1/4 / 1/2 =", y / x)
    print("1/2 / 4 =", x / 4)

    print("Is 2/4 equal 1/2?: ", Fraction(2, 4) == Fraction(1, 2))
    print("Is 4/2 equal 2?: ", Fraction(4, 2) == 2)
    print("Is 2 equal 4/2?: ", 2 == Fraction(4, 2))
    print("Is 3/2 equal 1/2?: ", Fraction(3, 2) == Fraction(1, 2))

    print("Is 1/2 bigger then 1/4?: ", x.is_bigger(y))
    print("Is 1/4 bigger then 1/2?: ", y.is_bigger(x))
