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
  println!("{:?}", map);
  // 남은건 독서실에서 졸리면 완성하기
}