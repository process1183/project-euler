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

#[derive(Serialize, Deserialize, Debug)]
struct LibeulerAnswers {
    factors: HashMap<u64, Vec<u64>>,
    fibonacci: Vec<u64>,
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
