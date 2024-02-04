from flask import Flask

app = Flask(__name__)

@app.route('/register')
def register():
    return """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <link rel="stylesheet" href="style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<style>*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins',sans-serif;
}
body{
    background-image: url( {{ url_for('static', filename='tablet2') }} );;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
.header{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 20px 100px;
    background: transparent;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}
.header .logo{
    font-size: 16px;
    color: white;
    text-decoration: none;
}
.navbar a {
    position: relative;
    font-size: 16px;
    color: aliceblue;
    text-decoration: none;
    font-weight: 500;
    margin-right: 30px;
}
.navbar a::after{
    content: '';
    position: absolute;
    left: 0;
    bottom: -6px;
    width: 100%;
    height: 2px;
    background: white;
    border-radius: 5px;
    transform: translateY(10px);
    opacity: 0;
    transition: .5s;
}
.navbar a:hover::after{
    transform: translateY(0);
    opacity: 1;
}  
.wrapper, .wrapper2{
    position: relative;
    width: 420px;
    background: transparent;
    border: 2px solid rgba(255, 255, 255, .2);
    backdrop-filter: blur(20px);
    box-shadow: 0 0 10px rgba(0,0,0,.2);
    color: rgb(15, 1, 1);
    border-radius: 10px;
    padding: 30px 40px;
    overflow: hidden;
}
.wrapper h1, .wrapper2 h1{
    font-size: 36px;
    text-align: center;
}
.wrapper .input-box, .wrapper2 .input-box{
    position: relative;
    width: 100%;
    height: 50px;
    background: transparent;
    margin: 30px 0;
}
.input-box input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    border: 2px solid gray;
    border-radius: 40px;
    font-size: 16px;
    color: rgb(0, 5, 8);
    padding: 20px 45px 20px 20px;
}
.input-box input::placeholder{
    color: rgb(1, 8, 14);
}
.input-box i{
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
}
.wrapper .remember-forgot{
    display: flex;
    justify-content: space-between;
    font-size: 14.5px;
    margin: -15px 0 15px;
}
.remember-forgot label input{
    accent-color: white;
    margin-right: 3px;
}
.remember-forgot a{
    color: rgb(15, 1, 1);
    text-decoration: none;
}
.remember-forgot a:hover{
    text-decoration: underline;
}
.wrapper .btn, .wrapper2 .btn{
    width: 100%;
    height: 45px;
    background: rgb(10, 0, 0);
    border: none;
    outline: none;
    border-radius: 40px;
    box-shadow: 0 0 10px black;
    cursor: pointer;
    font-size: 16px;
    color: #f5f2f2;
    font-weight: 600;
}
.wrapper .register-link, .wrapper2 .login-link{
    font-size: 14.5px;
    text-align: center;
    margin-top: 20px 0 15px;
}
.register-link p a, .login-link p a{
    color: rgb(14, 1, 1);
    text-decoration: none;
    font-weight: 600;
}
.register-link p a:hover, .login-link p a:hover{
    text-decoration: underline;
}</style>
<body>
    


<div class="wrapper2">
    
    <form action="">
        <h1>Registration</h1>
        <div class="input-box">
            <input type="text" placeholder="Username" required>
            <i class='bx bxs-user'></i>

        </div>
        <div class="input-box">
            <input type="email" placeholder="Email" required>
            <i class='bx bx-envelope' ></i>
            
        </div>
        <div class="input-box">
            <input type="text" placeholder="Reg ID">
            <i class='bx bx-id-card'></i>
        </div>
        <div class="input-box">
            <input type="password" placeholder="Password" required>
            <i class='bx bx-window-close'></i>
        </div>
        <button type="submit" class="btn">Register</button>
        <div class="login-link">
            <p>Already have an account?
                <a href="/">Login</a>
            </p>
        </div>
        
    </form>
</div>
</body>"""

@app.route('/')
def index():
    return """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E Prescription</title>
    <link rel="stylesheet" href="style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins',sans-serif;
}
body{
    background-image: url('tablet2.jpg');
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}
.header{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 20px 100px;
    background: transparent;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 99;
}
.header .logo{
    font-size: 16px;
    color: white;
    text-decoration: none;
}
.navbar a {
    position: relative;
    font-size: 16px;
    color: aliceblue;
    text-decoration: none;
    font-weight: 500;
    margin-right: 30px;
}
.navbar a::after{
    content: '';
    position: absolute;
    left: 0;
    bottom: -6px;
    width: 100%;
    height: 2px;
    background: white;
    border-radius: 5px;
    transform: translateY(10px);
    opacity: 0;
    transition: .5s;
}
.navbar a:hover::after{
    transform: translateY(0);
    opacity: 1;
}  
.wrapper, .wrapper2{
    position: relative;
    width: 420px;
    background: transparent;
    border: 2px solid rgba(255, 255, 255, .2);
    backdrop-filter: blur(20px);
    box-shadow: 0 0 10px rgba(0,0,0,.2);
    color: rgb(15, 1, 1);
    border-radius: 10px;
    padding: 30px 40px;
    overflow: hidden;
}
.wrapper h1, .wrapper2 h1{
    font-size: 36px;
    text-align: center;
}
.wrapper .input-box, .wrapper2 .input-box{
    position: relative;
    width: 100%;
    height: 50px;
    background: transparent;
    margin: 30px 0;
}
.input-box input{
    width: 100%;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    border: 2px solid gray;
    border-radius: 40px;
    font-size: 16px;
    color: rgb(0, 5, 8);
    padding: 20px 45px 20px 20px;
}
.input-box input::placeholder{
    color: rgb(1, 8, 14);
}
.input-box i{
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
}
.wrapper .remember-forgot{
    display: flex;
    justify-content: space-between;
    font-size: 14.5px;
    margin: -15px 0 15px;
}
.remember-forgot label input{
    accent-color: white;
    margin-right: 3px;
}
.remember-forgot a{
    color: rgb(15, 1, 1);
    text-decoration: none;
}
.remember-forgot a:hover{
    text-decoration: underline;
}
.wrapper .btn, .wrapper2 .btn{
    width: 100%;
    height: 45px;
    background: rgb(10, 0, 0);
    border: none;
    outline: none;
    border-radius: 40px;
    box-shadow: 0 0 10px black;
    cursor: pointer;
    font-size: 16px;
    color: #f5f2f2;
    font-weight: 600;
}
.wrapper .register-link, .wrapper2 .login-link{
    font-size: 14.5px;
    text-align: center;
    margin-top: 20px 0 15px;
}
.register-link p a, .login-link p a{
    color: rgb(14, 1, 1);
    text-decoration: none;
    font-weight: 600;
}
.register-link p a:hover, .login-link p a:hover{
    text-decoration: underline;
}</style>
<body>
    <header class="header">
        <a href="#" class="logo"><h3>E-Prescription</h3></a>
        <nav class="navbar">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
        </nav>
       
    </header>






    <div class="wrapper">
        
        <form action="">
            <h1>Login</h1>
            <div class="input-box">
                <input type="text" placeholder="Username" required>
                <i class='bx bxs-user'></i>

            </div>
            <div class="input-box">
                <input type="password" placeholder="Password" required>
                <i class='bx bxs-lock-alt'></i>
            </div>
            <div class="remember-forgot">
                <label> <input type="checkbox">Remember Me</label>
                <a href="#">Forgot password?</a>
            </div>
            <button type="submit" class="btn">Login</button>
            <div class="register-link">
                <p>Don't have an account?
                    <a href="/register">Register</a>
                </p>
            </div>
        </form>
        
    </div>
   
           

</body>"""


if __name__ == '__main__':
    app.run(debug=True)