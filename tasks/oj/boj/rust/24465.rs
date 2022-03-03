use std::{io, cmp::Ordering};

fn main() {
  let mut gets = String::new();
  let mut constells: Vec<bool> = vec![false; 12];
  let mut passes: Vec<(i32, i32)> = Vec::new();
  for _i in 0..7 {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let (m, d) = {
      let split: Vec<i32> = gets.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    constells[(get_constells(m, d)-1) as usize] = true;
  }
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let n = gets.trim().parse::<i32>().unwrap();
  for _i in 0..n {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let (m, d) = {
      let split: Vec<i32> = gets.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    if !constells[(get_constells(m, d)-1) as usize] {
      passes.append(&mut vec![(m, d)]);
    }
  }
  passes.sort_by(|a, b| {
    match (a.0).cmp(&b.0) {
      Ordering::Equal => (a.1).cmp(&b.1),
      other => other
    }
  });
  for i in 0..passes.len() {
    println!("{} {}", passes[i as usize].0, passes[i as usize].1);
  }
  if passes.len() == 0 { println!("ALL FAILED"); }
}

fn get_constells(m: i32, d: i32) -> i32 {
  if m <= 1 && d <= 19 { return 12 }
  else if m <= 1 || (m <= 2 && d <= 18) { return 1 }
  else if m <= 2 || (m <= 3 && d <= 20) { return 2 }
  else if m <= 3 || (m <= 4 && d <= 19) { return 3 }
  else if m <= 4 || (m <= 5 && d <= 20) { return 4 }
  else if m <= 5 || (m <= 6 && d <= 21) { return 5 }
  else if m <= 6 || (m <= 7 && d <= 22) { return 6 }
  else if m <= 7 || (m <= 8 && d <= 22) { return 7 }
  else if m <= 8 || (m <= 9 && d <= 22) { return 8 }
  else if m <= 9 || (m <= 10 && d <= 22) { return 9 }
  else if m <= 10 || (m <= 11 && d <= 22) { return 10 }
  else if m <= 11 || (m <= 12 && d <= 21) { return 11 }
  else { return 12 }
}