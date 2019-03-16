// Project Euler - Problem 5
// https://projecteuler.net/problem=5
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
use libeuler::{factor, lcm};


fn get_list(ulimit: u64) -> Vec<u64> {
    let mut v: Vec<u64> = (1..=ulimit).rev().collect();

    for i in (1..=ulimit).rev() {
        if !v.contains(&i) {
            continue;
        }
        let mut f = factor(i);
        let p = f.iter().position(|&x| x == i).unwrap();
        f.remove(p);
        for n in f.iter() {
            if let Some(pos) = v.iter().position(|&x| x == *n) {
                v.remove(pos);
            }
        }
    }

    v
}


fn main() {
    let l = get_list(20);
    let res = l.iter().fold(1, |acc, x| lcm(acc, *x));
    println!("{}", res);
}
