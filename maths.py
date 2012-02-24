#!/usr/bin/env python

import random

class Maths:
    """Static mathematical helper functions for RSA encryption"""

    @staticmethod
    def probably_prime(p):
        """Fermat's Primality Test"""
        for i in range(0, 50):
            a = random.randint(2, p-1)
            if Maths.powermod(a, (p - 1), p) != 1:
                return False
        return True

    @staticmethod
    def powermod(a, p, m):
        """Right-to-left binary method for modular exponentiation"""
        if p == 0: return 1

        if (p & 1) == 1:
            return (a * Maths.powermod((a * a) % m, p >> 1, m)) % m
        else:
            return 1 * Maths.powermod((a * a) % m, p >> 1, m)

    @staticmethod
    def is_coprime(a, b):
        if b == 0: return a == 1
        return Maths.is_coprime(b, a % b)

    @staticmethod
    def extended_gcd(a, b):
        """Find Greatest Common Divisor"""
        x = 0
        y = 1
        lastx = 1
        lasty = 0

        while b != 0:
            quotient = a / b
            temp = b
            b = a % b
            a = temp

            temp = x
            x = lastx - quotient * x
            lastx = temp

            temp = y
            y = lasty - quotient * y
            lasty = temp

        return lastx, lasty, a

    @staticmethod
    def next_prime(p):
        """Get the next prime number from the given odd number"""
        if p < 4: return p

        while True:
            if Maths.probably_prime(p):
                return p
            else:
                return Maths.next_prime(p + 2)

    @staticmethod
    def generate_prime(bitlength):
        """Generate a prime number of the given bitlength"""
        p = 1
        for x in range(0, bitlength):
            p = p * 2 + random.randint(0, 1)
        p = (p << 1) + 1

        return Maths.next_prime(p)
