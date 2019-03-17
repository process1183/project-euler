// Project Euler - Problem 7
// https://projecteuler.net/problem=7
//
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
use libeuler::is_prime;

fn main() {
    let prime_n = 10_001;

    let mut c = 0;
    let mut i = 0;
    while c < prime_n {
        i += 1;
        if is_prime(i) {
            c += 1
        }
    }

    println!("{}", i);
}
