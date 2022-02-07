// 틀렸습니다
use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let origin = String::from(puts);
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let n: i32 = puts.trim().parse::<i32>().unwrap();
  let mut changes: Vec<String> = Vec::new();
  let mut scales: Vec<i32> = Vec::new();
  for _ in 0..n {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let (change, scale): (String, i32) = {
      let split: Vec<&str> = puts.split_whitespace().collect();
      (String::from(split[0]), split[1].parse::<i32>().unwrap())
    };
    changes.append(&mut vec![String::from(change)]);
    scales.append(&mut vec![scale]);
  }
  let mut can: Vec<(i32, i32)> = Vec::new(); // can.0 = idx, can.1 = differ
  for i in 0..n {
    let origin_char: Vec<String> = origin.trim().chars()
      .map(|x| x.to_string())
      .collect();
    let change_char: Vec<String> = changes[i as usize].trim().chars()
      .map(|x| x.to_string())
      .collect();
    let mut origin_pointer = 0;
    let mut differ = 0;
    for j in 0..changes[i as usize].len() {
      if origin_pointer == origin_char.len() { 
        differ += 1;
        continue;
      }
      if change_char[j as usize] == origin_char[origin_pointer as usize] {
        origin_pointer += 1;
      } else {
        differ += 1;
      }
    }
    if origin_pointer == origin_char.len() {
      can.append(&mut vec![(i, differ)]);
    }
  }
  if can.len() == 0 {
    println!("No Jam");
    return
  }
  can.sort_by_key(|k| scales[k.0 as usize]/k.1);
  can.reverse();
  let mut can_filtered: Vec<i32> = vec![can[0].0];
  let max_gsb = scales[can[0].0 as usize]/can[0].1;
  for i in 1..can.len() {
    if max_gsb == scales[can[i as usize].0 as usize]/can[i as usize].1 {
      can_filtered.append(&mut vec![can[i as usize].0]);
    }
  }
  can_filtered.sort();
  println!("{}", changes[can_filtered[0] as usize]);
}