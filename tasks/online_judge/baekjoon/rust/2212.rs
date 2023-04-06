use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  io::stdin().read_line(&mut gets).ok();
  let (n, k) = {
    let split: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1])
  };
  gets.clear();
  io::stdin().read_line(&mut gets).ok();
  let mut sensors: Vec<i32> = gets.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect();
  sensors.sort();

  if k >= n {
    println!("0");
    return;
  }

  let mut dist: Vec<i32> = Vec::new();
  for i in 1..n {
    dist.append(&mut vec![sensors[i as usize] - sensors[(i-1) as usize]]);
  }
  dist.sort();
  dist.reverse();
  for _i in 0..k-1 {
    dist.remove(0);
  }

  println!("{}", dist.iter().sum::<i32>());
}