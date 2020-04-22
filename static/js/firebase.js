var app_fireBase = {} ;


(function(){
   
    var firebaseConfig = {
        apiKey: "AIzaSyBrpWA8Hx4AOM3fhVpMrp_tTHgvV_d1dFs",
        authDomain: "auth-c4ee3.firebaseapp.com",
        databaseURL: "https://auth-c4ee3.firebaseio.com",
        projectId: "auth-c4ee3",
        storageBucket: "auth-c4ee3.appspot.com",
        messagingSenderId: "37003437500",
        appId: "1:37003437500:web:deb0f3b993207a7b6377b9",
        measurementId: "G-R4SMVDDDHN"
      };
      
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      app_fireBase = firebase;

})()