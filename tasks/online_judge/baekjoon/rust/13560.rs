use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n = gets.trim().parse::<i32>().unwrap();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let mut split: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  split.sort();
  let mut sums = split[0];
  for i in 1..n {
    sums += split[i as usize];
    if (i * (i + 1) / 2) > sums {
      println!("-1");
      return
    }
  }
  if n * (n - 1) / 2 == sums {
    println!("1");
  } else {
    println!("-1");
  }
}