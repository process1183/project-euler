// Project Euler - Problem 1
// https://projecteuler.net/problem=1
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

fn main() {
    let limit = 1000;
    let n1 = 3;
    let n2 = 5;
    let n_min = std::cmp::min(n1, n2);

    let mut sum = 0;

    for i in (n_min..limit).rev() {
        if i % n1 == 0 || i % n2 == 0 {
            sum += i;
        }
    }

    println!("{}", sum);
}
