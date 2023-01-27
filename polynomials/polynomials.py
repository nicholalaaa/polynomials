class Polynomial:
    def __init__(self, coefs):
        self.coefficients = coefs
        self.degree = len(self.coefficients)-1

    def __str__(self):
        terms = [f"{c}x^{p}" for p, c in enumerate(self.coefficients)]
        return " + ".join(reversed(terms))

    def __repr__(self):
        return type(self).__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):
        return isinstance(other, Polynomial) and \
            self.coefficients == other.coefficients

    def __add__(self, other):
        if isinstance(other, Number):
            return Polynomial((self.coefficients[0]+other,) + self.coefficients[1:])
        if isinstance(other, Polynomial):
            common = min(self.degree, other.degree)+1
            coefs = tuple(a+b for a, b in zip(self.coefficients[:common], other.coefficients[:common]))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            return Polynomial(coefs)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __call__(self, value):
        return 1
