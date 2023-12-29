mod login;
mod asset_manager;
pub use login::open_ms_login;
use tauri::Manager;

#[macro_use]
extern crate dotenv_codegen;

// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#[cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn greet(name: &str) -> String {
  format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
async fn command_name(app: tauri::AppHandle) {
  tauri::WindowBuilder::new(
    &app,
    "external",
    tauri::WindowUrl::External(format!("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?prompt=select_account&client_id={}&response_type=code&scope=XboxLive.signin%20offline_access&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient", dotenv!("AZURE_CLIENT_ID")).parse().unwrap())
  ).build().unwrap();
}

fn main() {
  tauri::Builder::default()
    .setup(|app| {
      let id = app.listen_global("WINDOW_MOVED", |event| {
        println!("{:?}", event.payload())
      });
      asset_manager::init_assets(&mut app);
      Ok(())
    })
    .invoke_handler(tauri::generate_handler![greet])
    .invoke_handler(tauri::generate_handler![open_ms_login])
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}
