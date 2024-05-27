from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred=credentials.Certificate('sayfa\istanbul-bd37f-firebase-adminsdk-mrbss-1fd2eb9363.json')
firebase_admin.initialize_app(cred,{'databaseURL':"https://istanbul-bd37f-default-rtdb.firebaseio.com"})

ref=db.reference("/hesaplar")
print(ref.get())
