
import { initializeApp } from "firebase/app";

import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {

  apiKey: "AIzaSyBMNP5msn_lfJY1aLu5F-yhRnfXnQ7vU7A",

  authDomain: "samaritan-fc9b1.firebaseapp.com",

  projectId: "samaritan-fc9b1",

  storageBucket: "samaritan-fc9b1.firebasestorage.app",

  messagingSenderId: "401817678568",

  appId: "1:401817678568:web:35a0f351a0aa4dce9f0f5d",

  measurementId: "G-VSCFNR8GM7"

};

const app = initializeApp(firebaseConfig);

const analytics = getAnalytics(app);

