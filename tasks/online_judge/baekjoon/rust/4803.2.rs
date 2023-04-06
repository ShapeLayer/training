// WA: Wrong Answer

use std::io;

fn main() {
  let mut loops = 0;
  loop {
    loops += 1;
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).ok();
    let (n, m) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    if n == 0 && m == 0 { break; }
    let mut parents: Vec<i32> = (0..n+1).collect::<Vec<i32>>();
    let mut lines: Vec<i32> = vec![0; (n+1) as usize];
    for _i in 0..m {
      let mut puts = String::new();
      io::stdin().read_line(&mut puts).ok();
      let mut split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      split.sort();
      if parents[split[0] as usize] != parents[split[1] as usize] {
        lines[parents[split[0] as usize] as usize] += lines[parents[split[1] as usize] as usize];
        lines[parents[split[1] as usize] as usize] = 0;
      }
      lines[parents[split[0] as usize] as usize] += 1;
      let target_parent = parents[split[1] as usize];
      for i in 0..n+1 {
        if parents[i as usize] == target_parent {
          parents[i as usize] = parents[split[0] as usize];
        }
      }
    }
    let mut trees = 0;
    for i in 1..n+1 {
      if i != parents[i as usize] { continue; }
      let mut dots = 0;
      for j in i..n+1 {
        if parents[i as usize] == parents[j as usize] { dots += 1; }
      }
      if dots == lines[i as usize] + 1 { trees += 1; }
    }
    if trees == 0 {
      println!("Case {}: No trees.", loops);
    } else if trees == 1 {
      println!("Case {}: There is one tree.", loops);
    } else {
      println!("Case {}: A forest of {} trees.", loops, trees);
    }
  }
}