use std::{io, collections::HashMap};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let _n = puts.trim().parse::<i64>().unwrap();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let cards: Vec<i64> = puts.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let _m = puts.trim().parse::<i64>().unwrap();
  puts.clear();
  io::stdin().read_line(&mut puts).ok();
  let targets: Vec<i64> = puts.split_whitespace()
    .map(|x| x.parse::<i64>().unwrap())
    .collect();
  let mut counter = HashMap::new();
  for card in cards {
    let counts = counter.entry(card).or_insert(0);
    *counts += 1;
  }
  let mut res: Vec<i64> = Vec::new();
  for target in targets {
    res.append(&mut vec![*counter.entry(target).or_insert(0)]);
  }
  println!("{}", res.iter().map(|x| (*x).to_string()).collect::<Vec<String>>().join(" "));
}