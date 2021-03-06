use libeuler::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs;
use std::path::PathBuf;

// Test data JSON file path, relative to Cargo manifest dir
const TEST_DATA: &str = "tests/libeuler_test_data.json";

#[test]
fn fibonacci_sequence() {
    let answers = load_data(TEST_DATA).unwrap();
    for (i, v) in answers.fibonacci.iter().enumerate() {
        assert_eq!(nth_fibonacci(i as u32), *v);
    }
}

#[test]
fn primes() {
    let answers = load_data(TEST_DATA).unwrap();
    let upper_limit = *answers.primes.last().unwrap();
    let mut computed = Vec::new();
    for i in 0..=upper_limit {
        if is_prime(i as u64) {
            computed.push(i as u64);
        }
    }
    assert_eq!(computed, answers.primes);

    for i in &answers.primes_random {
        assert_eq!(is_prime(*i), true);
    }
}

#[test]
fn prime_factors() {
    let answers = load_data(TEST_DATA).unwrap();
    for i in &answers.primes {
        assert_eq!(prime_factor(*i), vec![*i]);
    }

    for (key, value) in &answers.prime_factors {
        assert_eq!(prime_factor(*key), *value);
    }
}

#[test]
fn reverse_ints() {
    let answers = load_data(TEST_DATA).unwrap();
    for (num, mun) in answers.reversed_ints.iter() {
        assert_eq!(reverse_int(*num), *mun);
    }
}

#[test]
fn palindromes() {
    let answers = load_data(TEST_DATA).unwrap();
    let upper_limit = *answers.palindromes.last().unwrap();
    let mut computed = Vec::new();
    for i in 0..=upper_limit {
        if is_palindrome(i as u64) {
            computed.push(i as u64);
        }
    }
    assert_eq!(computed, answers.palindromes);
}

#[test]
fn factors() {
    let answers = load_data(TEST_DATA).unwrap();
    for i in &answers.primes {
        assert_eq!(factor(*i), vec![1, *i]);
    }

    for (key, value) in &answers.factors {
        assert_eq!(factor(*key), *value);
    }
}

#[test]
fn gcds() {
    for i in 0..100 {
        assert_eq!(gcd(0, i), i);
        assert_eq!(gcd(i, 0), i);
        assert_eq!(gcd(1, i), 1);
        assert_eq!(gcd(i, 1), 1);
        assert_eq!(gcd(i, i), i);
    }

    let answers = load_data(TEST_DATA).unwrap();
    for i in &answers.gcds {
        assert_eq!(gcd(i[&'a'], i[&'b']), i[&'r']);
        assert_eq!(gcd(i[&'b'], i[&'a']), i[&'r']);
    }
}

#[test]
fn lcms() {
    for i in 0..100 {
        assert_eq!(lcm(0, i), 0);
        assert_eq!(lcm(i, 0), 0);
        assert_eq!(lcm(1, i), i);
        assert_eq!(lcm(i, 1), i);
        assert_eq!(lcm(i, i), i);
    }

    let answers = load_data(TEST_DATA).unwrap();
    for i in &answers.lcms {
        assert_eq!(lcm(i[&'a'], i[&'b']), i[&'r']);
        assert_eq!(lcm(i[&'b'], i[&'a']), i[&'r']);
    }
}

#[test]
fn prime_sieve() {
    let answers = load_data(TEST_DATA).unwrap();
    let limit = (*answers.primes.last().unwrap() as usize) + 1;
    let sieve = sieve_of_eratosthenes(limit);
    for (i,v) in answers.primes.iter().enumerate() {
        assert_eq!(sieve[i], *v as usize);
    }
}

#[derive(Serialize, Deserialize, Debug)]
struct LibeulerAnswers {
    factors: HashMap<u64, Vec<u64>>,
    fibonacci: Vec<u64>,
    gcds: Vec<HashMap<char, u64>>,
    lcms: Vec<HashMap<char, u64>>,
    palindromes: Vec<u64>,
    prime_factors: HashMap<u64, Vec<u64>>,
    primes: Vec<u64>,
    primes_random: Vec<u64>,
    reversed_ints: Vec<(u64, u64)>,
}

fn load_data(filename: &str) -> Result<LibeulerAnswers, Box<std::error::Error>> {
    let mut file_path = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    file_path.push(filename);

    let s = fs::read_to_string(file_path)?;
    let la: LibeulerAnswers = serde_json::from_str(&s)?;

    Ok(la)
}
