# Description: Integer Factorisation Using Trial Division Algorithm

### Trial Division Algorithm
- Trial division is one of the most labourious but easiest to understand algorithm for integer factorisation.
- The essential idea behind trial division tests to see if an integer n, the integer to be factored, can be divided by
  each number in turn that is less than n. For example, for the integer n = 12, the only numbers that divide it are
  1,2,3,4,6,12. Selecting only the largest powers of primes in this list gives 12 = 3 × 4.
- Trial division is guaranteed to find a factor of n if there is one, since it checks all possible prime factors of n.
  Thus, if the algorithm finds one factor, n, it is proof that n is a prime. If more than one factor is found, then n
  is a composite integer.
- This is quite a satisfactory algorithm, considering that even the best known algorithms have exponential time growth.
  For a chosen uniformly at random from integers of a given length, there is a 50% chance that 2 is a factor of a, and
  a 33% chance that 3 is a factor of a, and so on. It can be shown that 88% of all positive integers have a factor under
  100, and that 92% have a factor under 1000. Thus, when confronted by an arbitrary large a, it is worthwhile to check
  for divisibility by the small primes, since for a = 1000, in base-2 n=10.
- However, many-digit numbers that do not have factors in the small primes can require days or months to factor with
  trial division. In such cases other methods are used such as the quadratic sieve and the general number field sieve
  (GNFS).
- The largest cryptography-grade number that has been factored is RSA-768, using the GNFS and a network of hundreds of
  computers. The running time was approximately 2 years.

### Algorithm
* Input(s)
    - An integer n
* Output
    - A list of prime factors of n
* Algorithm
    1. Return "No Prime Factors" if n < 2.
    2. For i = 2 to n
        1. Exit if i * i > n
        2. Repeat till n % p == 0
            1. Add i to the list of prime factors.
            2. Set n = n / i
        3. break if n = 1. All prime factors have been found. Hence no need to continue.
    3. Add n to the list of prime factors if n > 1.
    4. Return the list of prime factors

### Optimisation(s)
1. One should always start from 2 onwards instead of backwards from n because an arbitrary n is more likely to be
   divisible by 2 than by 3, and so on.
2. There is no point in testing for divisibility by 4 if the number has already been determined not divisible by two,
   and so on for three and any multiple of three, etc. Therefore, effort can be reduced by selecting only prime numbers
   as candidate factors.
3. The trial factors need go no further than  √n because, if n is divisible by some number p, then n = p × q and if q
   were smaller than p, n would have earlier been detected as being divisible by q or a prime factor of q.
4. A definite bound on the prime factors is possible. Suppose P<sub>i</sub> is the i'th prime, so that P1 = 2, P2 = 3,
   P3 = 5, etc. Then the last prime number worth testing as a possible factor of n is P<sub>i</sub> where
   P<sup>2</sup><sub>i + 1</sub> > n; equality here would mean that P<sub>i + 1</sub> is a factor. Thus, testing with
   2, 3, and 5 suffices up to n = 48 not just 25 because the square of the next prime is 49, and below n = 25 just 2 and
   3 are sufficient. Should the square root of n be integral, then it is a factor and n is a perfect square.

### Complexity
- Worst case time complexity:
    - 2<sup>n/2</sup> if the algorithm is used without primality testing, but simply dividing by every odd number less
      than the square root of the base-2 n-digit number a, prime or not.
    - 2<sup>n/2</sup> / (n/2) ln 2 for a base-2 n-digit number a, if it starts from two and works up to the square root
      of a.
    - The time grows exponentially with the digits of the number in both the cases.
- Best case time complexity: NA
- Average case time complexity: NA

- Worst case space complexity: NA

### Interesting URLs
- None

### Note
- None

### TODO
- Add a solution with optimisation.
