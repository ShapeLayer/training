use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).ok();
  let n = puts.trim().parse::<i32>().unwrap();
  let mut i = 0;
  let mut flag = true;
  while i < n {
    let mut num = i;
    let mut res = 0;
    while num != 0 {
      res += num % 10;
      num /= 10;
    }
    res += i;
    if res == n { 
      println!("{}", i);
      flag = false;
      break;
    }
    i += 1;
  }
  if flag { println!("0"); }
}