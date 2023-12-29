use std::collections::HashMap;
use dotenv::dotenv;
use aimless_next_net;

#[tauri::command]
pub async fn open_ms_login(app: tauri::AppHandle) {
  tauri::WindowBuilder::new(
    &app,
    "external",
    tauri::WindowUrl::External(format!("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?prompt=select_account&client_id={}&response_type=code&scope=XboxLive.signin%20offline_access&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient", dotenv!("AZURE_CLIENT_ID")).parse().unwrap())
  )
    .on_navigation(|url| {
      println!("{:}", url);
      if url.host_str() == Some("login.microsoftonline.com") && url.path() == "/common/oauth2/nativeclient" {
        let hash_query: HashMap<_, _> = url.query_pairs().into_owned().collect();
        println!("{:}", hash_query.get("code").unwrap());
        return true;
      }
      true
    })
    .build().unwrap();
}
