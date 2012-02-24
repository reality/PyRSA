from maths import Maths

class Key:
    """Generates an RSA key pair"""

    def __init__(self, bitlength, private, public):
        self.bitlength = bitlength
        self.private = private
        self.public = public

    @staticmethod
    def generate_key(bitlength):
        e = 0
        while e == 0:
            p, q = Maths.generate_prime((int)(bitlength / 2)), \
                Maths.generate_prime((int)(bitlength / 2))
            n = p * q
            phi = ((p - 1) * (q - 1))

            # If it's not one of these might as well just restart
            if Maths.is_coprime(3, phi):
                e = 3
            elif Maths.is_coprime(17, phi):
                e = 17
            elif Maths.is_coprime(65537, phi):
                e = 65537

        gcd = Maths.extended_gcd(e, phi)
        d = (gcd[0] + phi) % phi

        private = [n, d]
        public = [n, e]

        return Key(bitlength, private, public)

key = Key.generate_key(1024)
print(key.private)
print(key.public)
