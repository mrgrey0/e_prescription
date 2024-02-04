from flask import Flask, redirect, render_template,request, url_for
import auth_methods

app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/homepage')
def homepage():
    return "WELCOME TO HOME PAGE"

@app.route('/regusr',methods =['GET','POST'])
def regusr():
    if request.method =='POST':
        username=request.form['email']
        password=request.form['password']
        res = auth_methods.signUp(username,password)
        if res =='success':
            return redirect(url_for('homepage'))
        elif res =='unsuccess':
            return "SOMETHING WENT WRONG"

@app.route('/loginChck',methods=['POST','GET'])
# pending user creating logi
def checklogin():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        res = auth_methods.login(username,password)
        if res=='success':
            return redirect(url_for('homepage'))
        elif res == 'unsuccess':
            return "<P>Something went wrong</P>"
    else :
        return "NONE"

if __name__ == '__main__':
    app.run(debug=True)