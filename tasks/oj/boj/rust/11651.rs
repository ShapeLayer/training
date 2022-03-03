use std::{io, cmp::Ordering};

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n = gets.trim().parse::<i32>().unwrap();
  let mut dots: Vec<(i32, i32)> = Vec::new();
  for _i in 0..n {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let (x, y) = {
      let split: Vec<i32> = gets.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    dots.append(&mut vec![(x, y)]);
  }
  dots.sort_by(|a, b| {
    match (a.1).cmp(&b.1) {
      Ordering::Equal => (a.0).cmp(&b.0),
      other => other
    }
  });
  for i in 0..n {
    println!("{} {}", dots[i as usize].0, dots[i as usize].1);
  }
}