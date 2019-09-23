import pyrebase
from flask import *

app = Flask(__name__)

firebaseConfig = {
    "apiKey": "AIzaSyDvoSkht9w_lKplATHdcruDlAR89jr0B3c",
    "authDomain": "testlog-e4fc6.firebaseapp.com",
    "databaseURL": "https://testlog-e4fc6.firebaseio.com",
    "projectId": "testlog-e4fc6",
    "storageBucket": "testlog-e4fc6.appspot.com",
    "messagingSenderId": "952906426220",
    "appId": "1:952906426220:web:0451df409be7fdb430f549"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

global db
db = firebase.database()
db.generate_key()


@app.route('/', methods=['GET', 'POST'])
def basic():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            user = auth.sign_in_with_email_and_password("python@testlog.com", "python")
            # user = auth.sign_in_with_email_and_password(email, password)
            global token
            token = user['idToken']
            # return getdata(user['idToken'], successful)
            return getdata(token, successful)
        except:
            return render_template('new.html', us=unsuccessful)
    return render_template('new.html')


def lsttostr(list):
    s = ""
    for i in list:
        s += i + "<br>"
    print(s)
    return s


def getdata(token, msg):
    users = db.child("cavaliers").get(token)
    l = [u.key() for u in users.each()]
    print(lsttostr(l))
    return render_template('new.html', dblist=l, s=msg)


def getinfos(user):
    ref = db.child("cavaliers").child(user)
    gotinfo = ref.get(token)
    print(gotinfo)
    s = ""
    lst = []
    for i in gotinfo.each():
        print(type(i.val()))
        if type(i.val()) == str:
            print("valeur : " + i.val())
            lst.append(i.key() + " : " + i.val())
            print(lst)
    s = lsttostr(lst)
    return (s)


@app.route("/infos", methods=['POST', 'GET'])
def infos():
    if request.method == 'POST':
        usr = request.form["caval_btn"]
        return getinfos(usr)


if __name__ == '__main__':
    app.run()

# usr = auth.sign_in_with_email_and_password(email, password)
#
# token = usr['idToken']
#
# print(auth.get_account_info(token))
#
# db = firebase.database()
# db.generate_key()
#
# users = db.child('cavaliers').get(token)
#
# for u in users.each():
#     print(u.key())
