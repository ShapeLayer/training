use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let n: i32 = puts.trim().parse::<i32>().unwrap();
  let mut arr: Vec<Vec<i32>> = Vec::new();
  for _ in 0..n {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).unwrap();
    let split: Vec<i32> = puts.split_whitespace()
      .map(|i| i.parse::<i32>().unwrap())
      .collect();
    arr.append(&mut vec![split]);
  }
}