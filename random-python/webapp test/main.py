from flask import Flask as flask

app = flask(__name__)

@app.route("/")
def home():
    x=input("Comment vous appelez-vous ?")
    return "Hello "+x

if __name__=="__main__":
    app.run(debug=True)
