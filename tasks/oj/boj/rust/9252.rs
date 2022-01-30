use std::io;

fn main() {
  let mut puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let str_a: Vec<String> = puts.trim().chars()
    .map(|i| i.to_string())
    .collect();
  puts = String::new();
  io::stdin().read_line(&mut puts).unwrap();
  let str_b: Vec<String> = puts.trim().chars()
    .map(|i| i.to_string())
    .collect();
  let n = str_a.len();
  let mut map: Vec<Vec<String>> = vec![vec![String::new(); n as usize]; n as usize];
  let mut dots: Vec<(i32, i32)> = Vec::new();
  for i in 0..n {
    for j in 0..n {
      if str_a[i as usize] == str_b[j as usize] {
        map[i as usize][j as usize] = str_a[i as usize].clone();
        dots.append(&mut vec![(i as i32, j as i32)]);
      }
    }
  }
  for dot in &dots {
    let (mut maximum, mut idx) = (String::new(), (0, 0));
    for target in &dots {
      if target.0 <= dot.0 && target.1 <= dot.1 {
        if map[target.0 as usize][target.1 as usize].len() > maximum.len() {
          maximum = map[target.0 as usize][target.1 as usize].clone();
          idx = *target;
        }
      }
    }
    map[dot.0 as usize][dot.1 as usize] = maximum.clone() + &map[dot.0 as usize][dot.1 as usize].clone();
    println!("dot: {:?}, mapcurr: {}", dot, map[dot.0 as usize][dot.1 as usize])
  }
  for arr in map {
    println!("{:?}", arr);
  }
  println!("{:?}", dots);
}