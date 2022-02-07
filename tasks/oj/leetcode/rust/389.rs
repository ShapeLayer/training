impl Solution {
  pub fn find_the_difference(s: String, t: String) -> char {
    let sc: u32 = s.chars()
      .map(|x| x as u32)
      .collect::<Vec<u32>>()
      .iter()
      .sum();
    let tc: u32 = t.chars()
      .map(|x| x as u32)
      .collect::<Vec<u32>>()
      .iter()
      .sum();
    char::from_u32(tc-sc).unwrap()
  }
}