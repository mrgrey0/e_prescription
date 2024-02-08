from flask import Flask, redirect, render_template,request, url_for
import auth_methods
#this is comment
app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def loginPg():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template("welcome.html")

@app.route('/homepage')
def homepage():
    return render_template("welcome.html")

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