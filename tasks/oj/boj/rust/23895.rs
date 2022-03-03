use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let t = gets.trim().parse::<i32>().unwrap();
  for i in 0..t {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let (n, b) = {
      let split: Vec<i32> = gets.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let mut arr: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    arr.sort();
    let mut budget = b;
    let mut counts = 0;
    for i in 0..n {
      budget -= arr[i as usize];
      counts += 1;
      if budget < 0 {
        counts -= 1;
        break;
      }
    }
    println!("Case #{}: {}", i+1, counts);
  }
}