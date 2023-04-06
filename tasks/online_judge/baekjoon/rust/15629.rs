use std::io;

fn main() {
  let mut gets = String::new();
  io::stdin().read_line(&mut gets).ok();
  let n: i32 = gets.trim().parse::<i32>().unwrap();
  let mut cost: i32 = 0;
  let mut prev: &str = ""; let mut prev_s: String = String::new();
  let mut ever_sa_visited: bool = false;
  for _i in 0..n {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    match gets.trim() {
      "botswana" => { cost += 0; }
      "ethiopia" => { cost += 50; }
      "kenya" => { cost += 50; }
      "namibia" => {
        if ever_sa_visited { cost += 40; }
        else { cost += 140; }
      }
      "south-africa" => {
        cost += 0;
        ever_sa_visited = true;
      }
      "tanzania" => { cost += 50; }
      "zambia" => { 
        if prev == "zimbabwe" { cost += 20; }
        else { cost += 50; }
      }
      "zimbabwe" => {
        if prev == "zambia" { cost += 0; }
        else { cost += 30; }
      }
      _ => {}
    }
    prev_s = gets.clone();
    prev = prev_s.trim();
  }
  println!("{}", cost);
}