use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let mut n: i64 = puts.trim().parse::<i64>().unwrap();
  let mut counts = 0;
  while n >= 5 {
    counts += n/5;
    n /= 5;
  }
  println!("{}", counts);
}