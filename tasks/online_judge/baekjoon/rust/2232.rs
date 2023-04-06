use std::io::{BufRead, BufWriter, Write};

fn main() {
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  let mut gets = String::new();
  stdin.read_line(&mut gets).ok();
  let n: i32 = gets.trim().parse().unwrap();
  let mut target: Vec<bool> = vec![false; n as usize];
  let mut prev = -1;
  for i in 0..n {
    gets.clear();
    stdin.read_line(&mut gets).ok();
    let pow: i32 = gets.trim().parse().unwrap();
    if pow >= prev {
      target[i as usize] = true;
      if prev != -1 { 
        if prev != pow {
          target[(i-1) as usize] = false;
        }
      }
    }
    prev = pow;
  }
  for i in 0..n {
    if target[i as usize] {
      writeln!(stdout, "{}", i+1);
    }
  }
}