pub fn init_assets(app: &mut tauri::App) {
  let resource_path = app.path_resolver()
    .app_data_dir();
  println!("{:}", resource_path.unwrap().into_os_string().into_string().unwrap());
}
