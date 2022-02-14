use std::{io, mem};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let split: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  let gcd = find_gcd(*split.iter().max().unwrap(), *split.iter().min().unwrap());
  println!("{}\n{}", gcd, gcd*(split[0]/gcd)*(split[1]/gcd));
}

fn find_gcd(mut big: i32, mut small: i32) -> i32 {
  while small != 0 {
    mem::swap(&mut big, &mut small);
    small %= big;
  }
  big
}