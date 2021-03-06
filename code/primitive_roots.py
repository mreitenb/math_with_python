# This code is not efficient for large values of n.
# But it's easy to find a primitive root of a safe prime,
# using the function primitive_root(safe_prime).
# To find a primitive root of any large prime p using the prime
# factorization of p-1, look in the file pohlig-hellman.py.

import random
# For cryptographically secure random number generation:
randint = random.SystemRandom().randint

from math import gcd
from utilities import prod
from primes import is_prime, make_prime, safe_prime
from factoring import list_of_prime_powers

def phi(n):
    # Euler's totient function
    assert(n > 0)
    counter = 0
    for k in range(0,n):
        if gcd(k,n) == 1:
            counter += 1
    return counter

def varphi(n):
    # More efficient implementation of Euler's totient function
    assert(n > 0)
    prime_powers = list_of_prime_powers(n)
    factors = [ (p-1)*pow(p,k-1) for (p,k) in prime_powers ]
    return prod(factors)

def order(a,n):
    # Returns the order of a (mod n)
    assert(n > 1)
    if gcd(a,n) != 1:
        raise Exception('Order is undefined')
    k = 1
    power = 1
    while True:
        power = (power * a) % n
        if power == 1:
            return k
        k += 1
        
def is_primitive_root(a,n):
    # Returns True if a is a primitive root (mod n)
    assert(n > 1)
    if gcd(a,n) != 1:
        return False
    return (order(a,n) == varphi(n))
            
def make_primitive_root(n):
    # Returns the smallest primitive root of n, or None
    assert(n > 1)
    for a in range(1,n):
        if is_primitive_root(a,n):
            return a
    return None

def has_primitive_root(n):
    # Returns True if n has a primitive root
    assert(n > 1)
    if make_primitive_root(n):
        return True
    return False

def primitive_root(safe_prime):
    # Returns a primitive root of a safe prime p
    p = safe_prime
    q = (p-1)//2
    assert(is_prime(p) and is_prime(q)) # making sure p is a safe prime
    while True:
        a = randint(2,p-2)
        if pow(a,2,p) !=1 and pow(a,q,p) != 1:
            return a
 
def make_base_point(d):
    # Returns a pair (p,r), where p is a safe prime
    # with d digits and r is a primitive roote of p
    p = safe_prime(d)
    r = primitive_root(p)
    return (p,r)
