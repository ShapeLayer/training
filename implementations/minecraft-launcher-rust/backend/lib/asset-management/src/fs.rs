use std::{path::PathBuf, io::Read};
use crate::definitions;

pub fn using(path: String) {
  std::fs::create_dir_all(path);
}

pub fn init_assets(config_root: &PathBuf, data_root: &PathBuf) {
  // Create directory
  std::fs::create_dir_all(config_root);
  std::fs::create_dir_all(data_root);

  // Load manifest.json
  let mut manifest_path = config_root.to_owned();
  manifest_path.push(definitions::MANIFEST_FILE_NAME);
  match std::fs::metadata(&manifest_path) {
    Ok(_) => {}
    Err(_) => {
      std::fs::File::create(&manifest_path);
    }
  }
  let mut f = std::fs::File::options()
    .read(true)
    .write(true)
    .open(&manifest_path)
    .unwrap();
  let mut gets: String = String::new();
  f.read_to_string(&mut gets).ok();
  let data: definitions::manifest = serde_json::from_str(&gets.as_str()).unwrap();
}
