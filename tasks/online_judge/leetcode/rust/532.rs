struct Solution {
}
impl Solution {
  pub fn find_pairs(nums: Vec<i32>, k: i32) -> i32 {
    let mut res: Vec<(i32, i32)> = Vec::new();
    for i in 0..nums.len() {
      for j in 1..nums.len() {
        if i == j { continue; }
        if (nums[i as usize] - nums[j as usize]).abs() == k {
          if res.contains(&(nums[i as usize], nums[j as usize])) || res.contains(&(nums[j as usize], nums[i as usize])) {
            continue;
          }
          res.append(&mut vec![(nums[i as usize], nums[j as usize])]);
        }
      }
    }
    res.len() as i32
  }
}

fn main() {
  Solution::find_pairs(vec![3, 1, 4, 1, 5], 2);
  Solution::find_pairs(vec![1, 2, 3, 4, 5], 1);
  Solution::find_pairs(vec![1, 3, 1, 5, 4], 0);
}