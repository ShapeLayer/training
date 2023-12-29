use std::collections::HashMap;
use reqwest;
use aimless_next_commons;

enum MicrosoftErrorCode {
  UNKNOWN,
  NO_PROFILE,
  NO_XBOX_ACCOUNT = 2148916233,
  XBL_BANNED = 2148916235,
  UNDER_18 = 2148916238
}

struct MicrosoftResponse<T> {
  data: T,
  responseStatus: RestResponseStatus
}

struct AbstractTokenRequest {
  client_id: String,
  scope: String,
  redirect_uri: String
}

struct getAccessTokenResult {
  data: HashMap,
  responseStatus: RestResponseStatus
}

struct MicrosoftAuth {
}

impl MicrosoftAuth {
  const TIMEOUT: i32 = 2500;

  const TOKEN_ENDPOINT: String = String::from("https://login.microsoftonline.com/consumers/oauth2/v2.0/token");
  const XBL_AUTH_ENDPOINT: String = String::from("https://user.auth.xboxlive.com/user/authenticate");
  const XSTS_AUTH_ENDPOINT: String = String::from("https://xsts.auth.xboxlive.com/xsts/authorize");
  const MC_AUTH_ENDPOINT: String = String::from("https://api.minecraftservices.com/authentication/login_with_xbox");
  const MC_ENTITLEMENT_ENDPOINT: String = String::from("https://api.minecraftservices.com/entitlements/mcstore");
  const MC_PROFILE_ENDPOINT: String = String::from("https://api.minecraftservices.com/minecraft/profile");

  const STANDARD_HEADER: HashMap<String, String> = HashMap::from([
    (String::from("Content-Type"), String::from("application/json")),
    (String::from("Accept"), String::from("application/json"))
  ]);
  
  /// Returns a MicrosoftResponse for this operation
  /// 
  /// # Arguments
  /// * `code` - Code Authorization Code or Refresh Token
  /// * `refresh` - `true` if this is a refresh, false otherwise.
  /// * `clientID` - Client ID The Azure application (client) ID.
  pub async fn getAccessToken(code: String, refresh: bool, client_id: String) {
    let form: HashMap<String, String> = HashMap::from([
      (String::from("client_id"), client_id),
      (String::from("scope"), String::from("XboxLive.signin")),
      (String::from("redirect_uri"), String::from("https://login.microsoftonline.com/common/oauth2/nativeclient"))
    ]);
    if (refresh) {
      form.insert(String::from("refresh_token"), code);
      form.insert(String::from("grant_type"), String::from("refresh_token"));
    } else {
      form.insert(String::from("code"), code);
      form.insert(String::from("grant_type"), String::from("authorization_code"));
    }

    let client = reqwest::Client::new();

    // Todo Later
    let resp = match client.post(TOKEN_ENDPOINT)
      .json(&form)
      .send()
      .await() {
        OK(resp) => {
          return resp.json();
        },
        Err(err) => panic!("Error: {}", err)
      };
  }

  /// Authenticate with Xbox Live with a Microsoft Access Token.
  pub async fn getXBLToken(access_token: String) {

  }
}
