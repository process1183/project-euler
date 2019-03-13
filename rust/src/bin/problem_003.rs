// Project Euler - Problem 3
// https://projecteuler.net/problem=3
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
use libeuler::prime_factor;

fn main() {
    let n = 600_851_475_143;
    let prime_factors = prime_factor(n);
    let largest = *prime_factors.iter().max().unwrap();

    println!("{}", largest);
}
