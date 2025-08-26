// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCZ7mZV_jaT53eFXmqEnu_rtgoStI-_6y4",
  authDomain: "kolli-hills-org.firebaseapp.com",
  projectId: "kolli-hills-org",
  storageBucket: "kolli-hills-org.firebasestorage.app",
  messagingSenderId: "36819625609",
  appId: "1:36819625609:web:dbc3c86dcd892cf5850858",
  measurementId: "G-MJKHECS37G"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export { app, analytics };
