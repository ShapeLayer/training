use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts);
  let puts: Vec<i32> = puts.split_whitespace()
    .map(|i| i.parse::<i32>().unwrap())
    .collect();
  //println!("{:.10}", puts[0] as f32/puts[1]);
  // => error[E0277]: cannot divide `f32` by `i32`
  //println!("{}", puts[0] as f32/puts[1] as f32);
  // => 0.33333334
  println!("{}", puts[0] as f64/puts[1] as f64);
}