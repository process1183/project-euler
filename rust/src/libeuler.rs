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
