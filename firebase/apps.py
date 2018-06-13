import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.apps import AppConfig

cred = credentials.Certificate("/home/prathik/demo/mysite/firebase/fir-74959-firebase-adminsdk-q68z2-346a2b1238.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref=db.collection(u'data').document(u'one')
doc_ref.set({
    u'stringExample': u'Hello, World!',
    u'booleanExample': True,
    u'numberExample': 3.14159265,
    u'arrayExample': [5, True, u'hello'],
    u'nullExample': None,
    u'objectExample': {
        u'a': 5,
        u'b': True
    }
})

doc_ref = db.collection(u'users').document(u'name1')
doc_ref.set({
    u'first': u'Prathik',
    u'last': u'Kumar',
    u'born': 1997
    })

doc_ref = db.collection(u'users').document(u'name2')
doc_ref.set({
    u'first': u'Rajath',
    u'last': u'Kumar',
    u'born': 1998
    })


class FirebaseConfig(AppConfig):
    name = 'firebase'
