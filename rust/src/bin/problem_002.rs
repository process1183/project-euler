// Project Euler - Problem 2
// https://projecteuler.net/problem=2
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
use libeuler::nth_fibonacci;

fn main() {
    let mut f = 0;
    let mut sum = 0;

    let mut i = 0;
    while f < 4_000_000 {
        f = nth_fibonacci(i);
        if f % 2 == 0 {
            sum += f;
        }
        i += 1;
    }

    println!("{}", sum);
}
