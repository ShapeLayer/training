use std::io;
use std::collections::HashMap;
static mut visited_dfs: Vec<i64> = vec!();
static mut visited_bfs: Vec<i64> = vec!();

fn main() {
  // Init
  let mut puts = String::new();
  io::stdin().read_line(&mut puts);
  let puts: Vec<usize> = puts.split_whitespace()
    .map(|i| i.parse::<usize>().unwrap())
    .collect();

  let (n, m, v) = (puts[0], puts[1], puts[2]);
  let mut hashmap: HashMap<usize, Vec<i64>> = HashMap::new();

  for _ in 0..m {
    let mut puts = String::new();
    io::stdin().read_line(&mut puts);
    let puts: Vec<usize> = puts.split_whitespace()
      .map(|i| i.parse::<usize>().unwrap())
      .collect();
    
    if !hashmap.contains_key(&puts[0]) {
      hashmap.insert(puts[0], Vec::new());
    }
    hashmap.get_mut(&puts[0]).unwrap().push(puts[1] as i64);
  }
  for (key, value) in &hashmap {
    println!("{}: {:?}", key, value);
  }

  // Call DFS
  dfs(v as i64, &hashmap);
  // Call BFS
}

fn dfs(n: i64, hashmap: &HashMap<usize, Vec<i64>>) {
  visited_dfs.append(&mut vec![n]);
  for dot in &hashmap[&(n as usize)] {
    if !visited_dfs.contains(&dot) {
      dfs(*dot as i64, &hashmap);
    }
  }
}

fn bfs() {}