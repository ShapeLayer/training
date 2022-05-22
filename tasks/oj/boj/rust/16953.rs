use std::{io, collections::VecDeque};

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (a, b) = {
    let split: Vec<i64> = gets.split_whitespace()
      .map(|x| x.parse::<i64>().unwrap())
      .collect();
    (split[0], split[1])
  };
  let mut queue: VecDeque<(i64, i64)> = VecDeque::new();
  queue.push_back((a, 1));
  while !queue.is_empty() {
    let now = queue.pop_front().unwrap();
    if now.0 == b {
      println!("{}", now.1);
      return;
    }
    if now.0 * 2 <= b { queue.push_back((now.0 * 2, now.1 + 1)); }
    if now.0 * 10 + 1 <= b { queue.push_back((now.0 * 10 + 1, now.1 + 1)); }
  }
  println!("-1");
}