// Project Euler Algorithms
// Copyright (C) 2019  Josh Gadeken
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

/// Calculate the Nth number in the Fibonacci sequence.
/// https://en.wikipedia.org/wiki/Fibonacci_number
pub fn nth_fibonacci(n: u32) -> u64 {
    if n == 0 || n == 1 {
        return u64::from(n);
    }

    let mut n1 = 0;
    let mut n2 = 1;
    let mut sum = 0;

    for _ in 1..n {
        sum = n1 + n2;
        n1 = n2;
        n2 = sum;
    }

    sum
}

/// Test if `n` is a prime number.
/// https://en.wikipedia.org/wiki/Prime_number
pub fn is_prime(n: u64) -> bool {
    match n {
        0 | 1 => return false,
        2 | 3 => return true,
        _ => (),
    }

    if n % 2 == 0 {
        return false;
    }

    let mut y = 3;
    let upper_limit = ((n as f64).sqrt() + 1.0) as u64;

    while y < upper_limit {
        if n % y == 0 {
            return false;
        } else {
            y += 2;
        }
    }

    true
}

/// Calculate the prime factors for a number.
/// https://en.wikipedia.org/wiki/Prime_factor
pub fn prime_factor(n: u64) -> Vec<u64> {
    let mut x = n;
    let mut y = 2;
    let mut pfs = Vec::new();

    while y <= x {
        if is_prime(y) && x % y == 0 {
            pfs.push(y);
            x /= y;
            y = 2;
            continue;
        }
        y += 1;
    }

    pfs.sort();

    pfs
}

/// Reverse digits in an integer
pub fn reverse_int(n: u64) -> u64 {
    let mut n = n;
    let mut r = 0;

    while n > 0 {
        r = (r * 10) + (n % 10);
        n /= 10;
    }

    r
}

/// Test if a number is palindromic.
/// https://en.wikipedia.org/wiki/Palindromic_number
pub fn is_palindrome(n: u64) -> bool {
    n == reverse_int(n)
}

/// Calculate the factors for a number.
/// https://en.wikipedia.org/wiki/Factorization
pub fn factor(n: u64) -> Vec<u64> {
    if n == 0 {
        return vec![];
    }
    let mut factors = vec![1, n];
    let mut y = 2;
    let upper_limit = (n as f64).sqrt() as u64;

    while y <= upper_limit {
        if n % y == 0 {
            factors.push(y);
            factors.push(n / y);
        }
        y += 1;
    }

    factors.sort();
    factors.dedup();

    factors
}

/// Compute the Greatest common divisor for `a` and `b`.
/// https://en.wikipedia.org/wiki/Greatest_common_divisor
pub fn gcd(a: u64, b: u64) -> u64 {
    let mut a = a;
    let mut b = b;
    let mut c;

    while b != 0 {
        c = a % b;
        a = b;
        b = c;
    }

    a
}

/// Compute the Least common multiple for `a` and `b`.
/// https://en.wikipedia.org/wiki/Least_common_multiple
pub fn lcm(a: u64, b: u64) -> u64 {
    if a == 0 || b == 0 {
        return 0;
    }

    (a / gcd(a, b)) * b
}

/// Generate prime numbers up to `limit`.
/// https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
pub fn sieve_of_eratosthenes(limit: usize) -> Vec<usize> {
    let mut sieve = vec![true; limit];
    sieve[0] = false;
    sieve[1] = false;

    let mut primes = Vec::new();

    for i in 0..sieve.len() {
        if sieve[i] {
            for n in (i.pow(2)..sieve.len()).step_by(i) {
                sieve[n] = false;
            }
            primes.push(i);
        }
    }

    primes
}
