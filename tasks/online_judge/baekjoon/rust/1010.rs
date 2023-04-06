use std::io;

fn main() {
  let mut n = String::new();
  io::stdin().read_line(&mut n);
  let m = n.trim().parse::<i32>().unwrap();
  for _ in 0..m {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts);
    let puts: Vec<i32> = puts.split_whitespace()
      .map(|i| i.parse::<i32>().unwrap())
      .collect();
    let mut calced: f64 = 1.0;
    let a = puts.iter().min().unwrap();
    let b = puts.iter().max().unwrap();
    for i in 0..*a {
      calced *= (*b-i) as f64/(i+1) as f64;
    }
    println!("{:.0}", calced);
  }
}