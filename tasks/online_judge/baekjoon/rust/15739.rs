use std::io;

fn main() {
  let mut n = String::new();
  io::stdin().read_line(&mut n);
  let n: i32 = n.trim().parse().unwrap();
  let mut map: Vec<Vec<i32>> = Vec::new();
  for _ in 0..n {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts);
    let puts: Vec<i32> = puts.split_whitespace()
      .map(|i| i.parse::<i32>().unwrap())
      .collect();
    map.append(&mut vec![puts]);
  }
  let mut flag: bool = true;
  let mut used: Vec<i32> = Vec::new();
  let mut sums: Vec<i32> = vec![n*(n*n+1)/2, 0, 0];
  for _ in 0..2*n { sums.append(&mut vec![0]); }
  for i in 0..n as usize {
    for j in 0..n as usize {
      if used.contains(&map[i][j]) {
        flag = false;
      } else {
        used.append(&mut vec![map[i][j]]);
      }
      if !(1..n*n+1).contains(&map[i][j]) {
        flag = false;
      }
      sums[i+3] += map[i][j]; sums[i+3+n as usize] += map[i][j];
      if i == j { sums[1] += map[i][j]; }
      if i+j+1 == n as usize { sums[2] += map[i][j]; }
      if !flag { break; }
    }
    if !flag { break; }
  }
  for i in 1..sums.iter().len() {
    if sums[0] != sums[i] {
      flag = false;
      break;
    }
  }
  println!("{}", if flag { "TRUE" } else { "FALSE" });
}