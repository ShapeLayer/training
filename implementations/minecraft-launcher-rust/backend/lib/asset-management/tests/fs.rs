extern crate aimless_next_asset_management;
use std::path::PathBuf;

#[test]
fn test_init() {
  aimless_next_asset_management::fs::init_assets(&PathBuf::from("./"), &PathBuf::from("./"));
}
