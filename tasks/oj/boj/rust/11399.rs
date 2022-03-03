use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n = gets.trim().parse::<i32>().unwrap();
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let mut arr: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  arr.sort();
  let mut sums = 0;
  for i in 0..n {
    sums += arr[i as usize] * (n-i);
  }
  println!("{}", sums);
}