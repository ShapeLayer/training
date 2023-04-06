use std::io;

fn main() {
  let mut gets = String::new();
  let mut dots: Vec<(i32, i32)> = Vec::new();
  for _i in 0..3 {
    gets.clear();
    io::stdin().read_line(&mut gets).ok();
    let dot: Vec<i32> = gets.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    dots.append(&mut vec![(dot[0], dot[1])]);
  }
  let op = (dots[0].0*dots[1].1 + dots[1].0*dots[2].1 + dots[2].0*dots[0].1) - (dots[0].0*dots[2].1 + dots[1].0*dots[0].1 + dots[2].0*dots[1].1);
  if op > 0 { println!("1"); }
  else if op < 0 { println!("-1"); }
  else { println!("0"); }
}