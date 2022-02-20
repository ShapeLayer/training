use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let (n, m) = {
    let split: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1])
  };
  let mut dots: Vec<(i32, i32, i32)> = Vec::new(); // x, y, order
  for i in 1..n+1 {
    puts.clear();
    io::stdin().read_line(&mut puts).ok();
    let (x, y) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    dots.append(&mut vec![(x, y, i)]);
  }
  for i in 0..n {}
  // 연결 여부 기록
  let mut is_conn: Vec<bool> = vec![false; (n+1) as usize];
  // 연결 맵 기록 [i, j] [j, i] 전부 기록할 것
  let mut conn_map: Vec<Vec<i32>> = vec![vec![false; (n+1) as usize]; (n+1) as usize];
  

}