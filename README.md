Python Code for Use in Number Theory and Cryptography 


utilities.py: Basic number theory utilities

    prod(numbers): Returns the product of a list of numbers

    egcd(a,b): Returns a triple (g,x,y) with g = gcd(a,b) = xa+yb

    modinv(a,m): Returns the modular inverse of a (mod m) between 0 and m

    chinese_remainder(a,m): Solves the system of congruences 
                x congruent a_i (mod m_i)
                where a = [ a_0, a_1, a_2, ... ]
                and   m = [ m_0, m_1, m_2, ... ] 
                    

primes.py: Primality testing and prime generation

    is_prime(n): Returns True if n is prime (Miller-Rabin test)
    
    make_prime(d): Creates a prime with d digits

    safe_prime(d): Creates a safe prime with d digits


factoring.py: Tools for finding the prime factorization

    find_factor(n): Uses Pollard's rho method to find a factor of n

    list_of_prime_factors(n): Returns the sorted list of all prime factors of n (with repetitions)

    list_of_prime_powers(n): Returns the prime factorization of n as a list (without repetitions)
                             of pairs (p,k), where p is a prime factor of multiplicity k

    print_prime_factorization(n): Prints the prime factorization of n


primitive_roots.py: Orders and primitive roots. Warning: Code not optimized for large n

    phi(n): Euler's totient function
    
    order(a,n): Returns the order of a (mod n)

    is_primitive_root(a,n): Returns True if a is a primitive root (mod n)

    make_primitive_root(n): Returns the smallest primitive root of n, or None

    has_primitive_root(n): Returns True if n has a primitive root


hashes.py: SHA-256 hashes

    sha_256_hex(string): Returns the SHA-256 hash of a string as a hexadecimal string  

    sha_256(string): Returns the SHA-256 hash of a string as a base 10 integer


rsa.py: RSA encryption and RSA signatures

    create_rsa_private_key(d): Creates a private RSA key (p,q,j) where p and q have d digits

    rsa_public_key(private_key): Returns the public key (n,k) corresponding to a private key (p,q,j)
    
    rsa_encrypt(plaintext, public_key): Encrypts an integer plaintext with a public key (n,k)
    
    rsa_decrypt(ciphertext, private_key): Decrypts an integer ciphertext with a private key (p,q,j)
    
    rsa_signature(string, private_key): Signs the SHA-256 hash of a string with a private key (p,q,j)
    
    rsa_verify(string, signature, public_key): Verifies if the SHA-256 hash of the string was
                                               correctly signed by the owner of the public key (n,k)


elgamal.py: ElGamal encryption and ElGamal signatures

    create_EG_private_key(): Creates an integer ElGamal private key
    
    EG_public_key(private_key): Returns the public key corresponding to a private key

    EG_encrypt(plaintext, public_key): ElGamal encryption of an integer plaintext with a public key
    
    EG_decrypt(ciphertext, private_key): ElGamal decryption of ciphertext (A,M) with a private key

    EG_sign(string, private_key): Signs the SHA-256 hash of a string with a private key
    
    EG_verify(string, signature, public_key): Verifies if the SHA-256 hash of the string was
                                              correctly signed by the owner of the public key


pohlig-hellman.py: Implementation of the Pohlig-Hellman algorithm to compute discrete logarithms


shamir_sharing.py: Implemetation of Shamir's Secret Sharing method


ecc.py: Tools for elliptic curve computations
