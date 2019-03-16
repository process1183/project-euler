// Project Euler - Problem 6
// https://projecteuler.net/problem=6
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
    let upper_limit: u64 = 100;
    let sum_of_squares: u64 = (1..=upper_limit).map(|n| n.pow(2)).sum();
    let square_of_sums: u64 = (1..=upper_limit).sum::<u64>().pow(2);
    let res = square_of_sums - sum_of_squares;

    println!("{}", res);
}
