use std::{io, cmp};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let (n, a, b) = {
    let split: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1], split[2])
  };
  let mut lectures: Vec<(i32, i32)> = Vec::new();
  for _i in 0..10 {
    puts.clear();
    io::stdin().read_line(&mut puts).ok();
    let (x, y) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    lectures.append(&mut vec![(x, y)]);
  }
  let mut total = 130 - b;
  let mut major = 66 - a;
  for i in 0..8-n {
    total -= cmp::min(lectures[i as usize].0 + lectures[i as usize].1, 6) * 3;
    major -= cmp::min(lectures[i as usize].0, 6) * 3;
  }
  if total <= 0 && major <= 0 { println!("Nice"); }
  else { println!("Nae ga wae"); }
}