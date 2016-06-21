# Problem Analysis

### Concepts/Theories

#### Prime Number Sieve or Prime Sieve
- A prime sieve or prime number sieve is a fast type of algorithm for finding primes.
- There are many prime sieves. The sieve of Eratosthenes (250s BC), the sieve of Sundaram (1934) are simple algorithms.
  The sieve of Atkin (2004) is a faster but complicated algorithm. Then there are various wheel sieves.
- A prime sieve works by creating a list of all integers up to a desired limit and progressively removing composite
  numbers (which it directly generates) until only primes are left. This is the most efficient way to obtain a large
  range of primes.

#### Sieve of Eratosthenes (250s BC)
- Sieve of Eratosthenes is an algorithm to find all the prime numbers between 1 and less than or equal to a given
  integer N.
- The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes.
- An Anonymous short mnemonic rhyme

    "Sift the Two's and Sift the Three's,

    The Sieve of Eratosthenes.

    When the multiples sublime,

    The numbers that remain are Prime."

### Analysis
* None


### Solution/Algorithm
<pre>
function sieve_of_eratosthenes(n)
    Input: 
        - (int) n = a number upto which prime numbers should be generated.
    Output: 
        - (int list) A list of prime numbers between 1 and N

    1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2. Initially, let p equal 2, the first prime number.
    3. Starting from p, enumerate its multiples by counting to n in increments of p, and mark them in the list 
       (these will be 2p, 3p, 4p, ... ; the p itself should not be marked).
    4. Find the FIRST number greater than p in the list that is not marked. If there was no such number, stop.
       Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
</pre>

### Optimisation(s)
1. As a refinement, it is sufficient to mark the numbers in step 3 starting from p<sup>2, as all the smaller multiples
   of p will have already been marked at that point. This means that the algorithm is allowed to terminate in step 4
   when p<sup>2 is greater than n.
2. Another refinement is to initially list odd numbers only, (3, 5, ..., n), and count in increments of 2p in step 3,
   thus marking only odd multiples of p.

### Complexity
* Worst case time complexity: O(n log log n)
* Best case time complexity: NA
* Average case time complexity: NA
* Worst case space complexity: NA

### Reference(s)
- [None](#)

### Note
- None

### TODO
- Implement optimisation 2.
- This takes a lot of memory for generating large range of prime numbers. Learn to use segmented sieve algorithm.
