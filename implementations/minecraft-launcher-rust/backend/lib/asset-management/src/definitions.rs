use serde::{Serialize, Deserialize};

pub const MANIFEST_FILE_NAME: &str = "manifest.json";

#[derive(Serialize, Deserialize, Debug)]
pub struct manifest<'a> {
  manifest_version: usize,
  index_server: &'a str,
}
pub const manifest_default: manifest = manifest {
  manifest_version: 1,
  index_server: "https://github.com/shapelayer/"
};
