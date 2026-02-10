#challenge_RationalNumbers.py



from math import gcd

class Rational:
    def __init__(self, p, q=1):
        self.p=p //gcd(p,q)
        self.q = q // gcd(p, q)

    def __add__(self, other):
        num = self.p * other.q + self.q * other.p
        den = self.q * other.q
        return Rational(num, den)
    
    def __mul__(self, other):
        num = self.p * other.p
        den = self.q * other.q
        return Rational(num, den)
    
    def __eq__(self, other):
        if self.p == other.p and self.q == other.q: 
            return True

        return False
    
    def __lt__(self, other):
        return self.p * other.q < self.q * other.p

    def __str__(self):
        return f"{self.p}/{self.q}"
    


#test
p = Rational(1,2)
q = Rational(2,3)

print(p)
print(q)
print(p+q)
print(p<q)