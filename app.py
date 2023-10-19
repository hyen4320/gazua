from flask import Flask,request, Response,render_template

app=Flask(__name__)
FLAG=open('flag/flag.txt','r').read()
users={'guest':'guest', 'admin':FLAG,'CHUA':'CHUA'}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/index")
def index():
    return "3M"

@app.route("/tirano")
def tirano():
    return "0078"

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        if id in users:
            pw_check = users[id]
            if pw == pw_check:
                resp=Response("login success")
                resp.set_cookie("ID",id)
                return resp
            else:
                return "Login failed"
        else:
            return "User not found"
    return render_template('login.html')
@app.route("/auth", methods=['GET','POST'])
def info():
    if request.method=='GET':
        auth_id=request.cookies.get('ID')
        if auth_id=="admin":
            return f"Hello admin the flag is {FLAG}"
        else:
            return "your not admin"
    
if __name__=="__main__":
    app.run()

        
