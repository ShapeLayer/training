use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts);
  let puts: Vec<i32> = puts.split_whitespace()
    .map(|i| i.parse::<i32>().unwrap())
    .collect();
  let mut total: i32 = puts[1]; let mut coin_cnt: i32 = 0;
  let mut coins: Vec<i32> = Vec::new();
  for _ in 0..puts[0] {
    let mut coin = String::new();
    io::stdin().read_line(&mut coin);
    let coin: i32 = coin.trim().parse().unwrap();
    coins.push(coin);
  }
  for i in (0..coins.len()).rev() {
    let cn: i32 = total / coins[i];
    if cn != 0 {
      coin_cnt += cn;
      total -= cn * coins[i];
    }
  }
  println!("{}", coin_cnt);
}