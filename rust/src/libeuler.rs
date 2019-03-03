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
