use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let t: i32 = puts.trim().parse::<i32>().unwrap();
  let mut counts: Vec<(i32, i32)> = vec![(0, 0); 41];
  counts[0] = (1, 0);
  counts[1] = (0, 1);
  for _ in 0..t {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).unwrap();
    let n: i32 = puts.trim().parse::<i32>().unwrap();
    for i in 2..n+1 {
      counts[i as usize] = {
        (counts[(i-1) as usize].0 + counts[(i-2) as usize].0, counts[(i-1) as usize].1 + counts[(i-2) as usize].1)
      }
    }
    println!("{} {}", counts[n as usize].0, counts[n as usize].1);
  }
}