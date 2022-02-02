use std::io;

fn main() {
  let mut cnt = 0;
  loop {
    cnt += 1;
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).unwrap();
    let n: i32 = puts.trim().parse::<i32>().unwrap();
    if n == 0 { return; }
    let mut names: Vec<String> = Vec::new();
    for _i in 0..n {
      let mut puts = String::new();
      io::stdin().read_line(&mut puts).unwrap();
      names.append(&mut vec![puts]);
    }
    let mut returns: Vec<i32> = vec![0; (n+1) as usize]; // 0: init, 1: taken, 2: returned
    for _i in 0..(2*n-1) {
      let mut puts = String::new();
      io::stdin().read_line(&mut puts).unwrap();
      let nn: i32 = {
        let split: Vec<String> = puts.split_whitespace()
          .map(|x| String::from(x))
          .collect();
        let nn: i32 = split[0].trim().parse::<i32>().unwrap();
        nn
      };
      returns[nn as usize] += 1;
    }
    for i in 1..n+1 {
      if returns[i as usize] == 1 {
        println!("{} {}", cnt, names[(i-1) as usize].trim());
        break;
      }
    }
  }
}