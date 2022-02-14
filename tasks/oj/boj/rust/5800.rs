use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let k: i32= puts.trim().parse::<i32>().unwrap();
  for i in 0..k {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let (n, mut arr): (i32, Vec<i32>) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1..].to_vec())
    };
    arr.sort();
    let mut gap: Vec<i32> = vec![0; (n-1) as usize];
    for i in 0..n-1 {
      gap[i as usize] = (arr[(i+1) as usize] - arr[i as usize]).abs();
    }
    println!("Class {}", i+1);
    println!("Max {}, Min {}, Largest gap {}", arr.iter().max().unwrap(), arr.iter().min().unwrap(), gap.iter().max().unwrap());
  }
}