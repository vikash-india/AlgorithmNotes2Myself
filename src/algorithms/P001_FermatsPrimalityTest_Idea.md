# Description: Fermat's Primality Test

### Fermat's Little Theorem (1640)
- Fermat's little theorem states that if p is a prime number, then for any integer a, the number a<sup>p</sup> − a is an
  integer multiple of p.
- Mathematically,

    a<sup>p</sup> ≡ a (mod p), for every 0 < a < p

    a<sup>p - 1</sup> ≡ 1 (mod p), for every 0 < a < p

- Carmichael numbers are COMPOSITE numbers which have the same above property of modular arithmetic congruence.
- If we want to test whether p is prime, then we can pick random a's in the interval and see whether the equality holds.
  If the equality does not hold for a value of a, then p is DEFINITELY composite. If the equality does hold for many
  values of a, then we can say that p is PROBABLY prime.

### Fermat Liar
- Any number a is called a Fermat Liar if, a<sup>n - 1</sup> ≡ 1 (mod n) when n is COMPOSITE.

### Fermat Pseudoprime
- Any COMPOSITE number n is called a Fermat pseudoprime to the base a if, a<sup>n - 1</sup> ≡ 1 (mod n).
- 341, 561, 645, 1105 etc are Fermat Pseudoprime.

### Carmichael Numbers
- A Carmichael number is an ODD composite number which satisfies the modular arithmetic congruence relation for all
  integers which are relatively prime to it.
- In simple terms, Carmichael numbers are Fermat pseudoprimes to every base co-prime to it and are also called absolute
  pseudoprimes. All Carmichael numbers are Fermat Pseudoprime but all Fermat Pseudoprime numbers are not Carmichael
  numbers.
- Carmichal Numbers: 561, 1105, 1729, 2465, 2821, 6601, 8911 etc.
- 561 is not prime since 561 = 3 x 11 x 17. But for the Fermat Liar, a = 2, 2<sup>561 - 1</sup> ≡ 1 (mod 561). 561 is
  Fermat Pseudoprime for every base that is co prime to 561.
- There are 585,355 Carmichael numbers up to 10^17.

### Fermat Witness
- Any number a is called Fermat Witness for the COMPOSITENESS  of n, if a<sup>n - 1</sup> ≢ 1 (mod n) when n is
  COMPOSITE.
