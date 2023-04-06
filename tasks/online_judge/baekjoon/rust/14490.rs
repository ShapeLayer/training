use std::{io, mem};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let split: Vec<i64> = puts.split(":")
    .map(|x| x.trim().parse::<i64>().unwrap())
    .collect();
  let gcd = find_gcd(*split.iter().max().unwrap(), *split.iter().min().unwrap());
  println!("{}:{}", split[0]/gcd, split[1]/gcd);
}

fn find_gcd(mut a: i64, mut b: i64) -> i64 {
  while b != 0 {
    mem::swap(&mut b, &mut a);
    b %= a;
  }
  a
}