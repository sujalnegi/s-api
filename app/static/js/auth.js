import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyB9NzjjEOcXD-CUbw7rolhYfFlQiBX4-rE",
  authDomain: "samaritan-fc9b1.firebaseapp.com",
  projectId: "samaritan-fc9b1",
  storageBucket: "samaritan-fc9b1.appspot.com",
  messagingSenderId: "401817678568",
  appId: "1:401817678568:web:35a0f351a0aa4dce9f0f5d"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
provider.setCustomParameters({ prompt: "select_account" });

async function signInWithGoogle() {
  try {
    const result = await signInWithPopup(auth, provider);
    const idToken = await result.user.getIdToken();
    const resp = await fetch("/api/session/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + idToken
      },
      body: JSON.stringify({})
    });
    if (resp.ok) {
      window.location.href = "/dashboard";
      return;
    }
    let data;
    try {
      data = await resp.json();
    } catch {
      data = { error: await resp.text() };
    }
    alert(data.error || "Login failed");
  } catch (err) {
    alert(err.message || "Sign in failed");
  }
}

function init() {
  const btn = document.getElementById("googleSignInBtn");
  if (!btn) return;
  btn.addEventListener("click", signInWithGoogle);
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}
