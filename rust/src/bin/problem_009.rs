// Project Euler - Problem 9
// https://projecteuler.net/problem=9
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
    for a in 1..500 {
        for b in a..500 {
            let c: u64 = 1_000 - b - a;
            if a.pow(2) + b.pow(2) == c.pow(2) {
                println!("{}", a * b * c);
                return;
            }
        }
    }
}
