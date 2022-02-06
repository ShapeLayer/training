use std::io::{BufRead, BufWriter, Write};

fn main() {
  let mut puts = String::new();
  let stdin = std::io::stdin();
  let mut stdin = stdin.lock();
  let stdout = std::io::stdout();
  let mut stdout = BufWriter::new(stdout.lock());
  stdin.read_line(&mut puts).ok();
  let n: i32 = puts.trim().parse::<i32>().unwrap();
  for _ in 0..n {
    puts.clear();
    stdin.read_line(&mut puts).ok();
    let (a, b) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    writeln!(stdout, "{}", a + b).ok();
  }
}