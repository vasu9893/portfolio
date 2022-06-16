
import email
from email import message
from flask import Flask , render_template ,url_for,redirect,request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/submit_form', methods = ['POST','GET'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        write_data(data)
        print (data)
        return "form submitted hooray"

    else :
        return "form not submitted"


def write_data(data):
    name = data['name']
    email = data['email']
    message = data["message"]
    with open('database.txt','a') as f:
        f.write("email:{},name:{},message: {}".format(email,name,message))

app.run(debug=True)


