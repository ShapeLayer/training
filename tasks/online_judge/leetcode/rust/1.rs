struct Solution {
}
impl Solution {
  pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    for i in 0..nums.len() {
      for j in 0..nums.len() {
        if i == j { continue; }
        if nums[i as usize] + nums[j as usize] == target {
          return vec![i as i32, j as i32];
        }
      }
    }
    vec![0, 0]
  }
}

fn main() {
  // Usage: Solution::two_sum(nums, target);

  // Debug
  /*
  println!("{:?}", Solution::two_sum(vec![2, 7, 11, 15], 9));
  println!("{:?}", Solution::two_sum(vec![3, 2, 4], 6));
  println!("{:?}", Solution::two_sum(vec![3, 3], 6));
  */
}