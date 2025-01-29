import api from './service'

function SingUp(username, userpass) {
    api()
}

function SetSessionCookie(username, userpass) {
    document.cookie = `
        username=${username};
        password=${userpass};
    `
}

function GetSession() {
    const cookies = document.cookie.split("; ");
    const session = {};
    cookies.forEach(cookie => {
      const [key, value] = cookie.split("=");
      session[key] = value;
    });
    return session;
  }

function clearOutputCookieValue() {
  const output = document.getElementById("cookie-value");
  output.textContent = "";
}