use std::io;

fn proc(a: i64, b_: i64, c: i64) -> i64 {
  if b_ == 1 { return a % c; }
  let k: i64 = proc(a, b_ / 2, c) % c;
  if b_ % 2 == 0 { return k * k % c; }
  else { k * k % c * a % c }
}

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (a, b, c) = {
    let split: Vec<i64> = gets.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
    (split[0], split[1], split[2])
  };
  println!("{}", proc(a, b, c));
}