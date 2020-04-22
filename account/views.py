from django.shortcuts import render
# from firebase import Firebase
import pyrebase

firebaseConfig = {
  'apiKey' : "AIzaSyBrpWA8Hx4AOM3fhVpMrp_tTHgvV_d1dFs",
  'authDomain': "auth-c4ee3.firebaseapp.com",
  'databaseURL': "https://auth-c4ee3.firebaseio.com",
  'projectId': "auth-c4ee3",
  'storageBucket': "auth-c4ee3.appspot.com",
  'messagingSenderId': "37003437500",
  'appId': "1:37003437500:web:deb0f3b993207a7b6377b9",
  'measurementId': "G-R4SMVDDDHN",
}

# firebase = Firebase(firebaseConfig)
firebase = pyrebase.initialize_app(firebaseConfig)

actionCodeSettings = {
  'url': 'https://www.example.com/finishSignUp?cartId=1234',
  'handleCodeInApp': True,

}

auth = firebase.auth()

# Create your views here.
def sigin(request):
    return render(request,'account/login.html') 

def welcome(request):
    return render(request,'account/welcome.html') 

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
       
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"account/login.html",{"msg":message})
        print(user)
    return render(request, "account/welcome.html",{"e":email})

