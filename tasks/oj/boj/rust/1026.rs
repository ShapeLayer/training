use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let n: i32 = puts.trim().parse::<i32>().unwrap();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let mut a: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let mut b: Vec<i32> = puts.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  a.sort();
  b.sort();
  b.reverse();
  let mut res: i32 = 0;
  for i in 0..n {
    res += a[i as usize] * b[i as usize];
  }
  println!("{}", res);
}