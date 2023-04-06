use std::{io, cmp};

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let (n, m): (i32, i32) = {
    let split: Vec<i32> = puts.split_whitespace()
      .map(|x| x.parse::<i32>().unwrap())
      .collect();
    (split[0], split[1])
  };
  let (mut package, mut indiv) = (0, 0);
  for i in 0..m {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts).unwrap();
    let (p_package, p_indiv) = {
      let split: Vec<i32> = puts.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
      (split[0], split[1])
    };
    if i == 0 {
      package = p_package;
      indiv = p_indiv;
    }
    else {
      package = cmp::min(package, p_package);
      indiv = cmp::min(indiv, p_indiv);
    }
  }
  let mut price = indiv * n;
  for i in 1..((n/6) as i32)+2 {
    price = cmp::min(price, i*package + cmp::max(n-i*6, 0)*indiv);
  }
  println!("{}", price);
}