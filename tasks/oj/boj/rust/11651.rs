// TO: TimeOut

use std::{io, collections::HashMap};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let n = puts.trim().parse::<i32>().unwrap();
  let mut dots: HashMap<i32, Vec<i32>> = HashMap::new(); // key: y
  for _i in 0..n {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let (x, y) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    let dot = dots.entry(y).or_insert(Vec::new());
    dot.append(&mut vec![x]);
  }
  let mut keys = dots.keys().cloned().collect::<Vec<i32>>();
  keys.sort();
  for key in keys {
    let arr = dots.entry(key).or_insert(Vec::new());
    arr.sort();
    for x in arr {
      println!("{} {}", x, key);
    }
  }
}