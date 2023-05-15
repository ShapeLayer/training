use std::io;

fn compute(a: i32, d: i32, k: i32) -> Option<i32> {
  let n = k - a + d;
  if n % d == 0 && n / d >= 1 { Some(n / d) } else { None }
}

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let (a, d, k): (i32, i32, i32) = {
    let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  match compute(a, d, k) {
    Some(x) => println!("{}", x),
    None => println!("X")
  }
}
