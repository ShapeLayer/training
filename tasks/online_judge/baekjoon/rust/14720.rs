use std::io;

fn compute(n: i32, markets: Vec<i32>) -> i32 {
  let mut counts: i32 = 0;
  let mut prev: i32 = -1;
  for i in 0..(n as usize) {
    counts += match markets[i] {
      0 => if (prev + 3) % 3 == 2 { 
        prev = markets[i];
        1
      } else { 0 }
      1 => if prev == 0 {
        prev = markets[i];
        1
      } else { 0 }
      2 => if prev == 1 {
        prev = markets[i];
        1
      } else { 0 }
      _ => 0
    };
  }
  counts
}

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n: i32 = gets.trim().parse::<i32>().unwrap();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let markets: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  let result = compute(n, markets);
  println!("{}", result);
}
