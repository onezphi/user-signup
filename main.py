from flask import Flask,render_template,request
# importing regular expression library 
import re
app=Flask(__name__)


# route to home page
@app.route('/',methods=['POST','GET'])
def index():
    # initializing errors at start
    nameerror=None
    passerror=None
    verifyerror=None
    emailerror=None
    # if form is submitted
    if request.method == 'POST':
        username=request.form['user']
        password=request.form['pass']
        verify_password=request.form['verify']
        email=request.form['email']
        # check for username
        if username == '' or len(username) < 3 or ' ' in username:
            nameerror='That\'s not a valid username'
            username=''
        # check for password    
        if password == '' or len(password) < 3 or  ' ' in password:
            passerror='That\'s not a valid password'
        # recheck for verifying password    
        if password != verify_password or verify_password == '':
            verifyerror='Passwords don\'t match'
        # check for email with regex    
        if email != '':
            if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) or len(email) > 20:
                emailerror='That\'s not a valid email'
                email=''
        # check to see if any of the error occurs            
        if nameerror or passerror or verifyerror or emailerror:

            return render_template('home.html',nameerror=nameerror,passerror=passerror,emailerror=emailerror,verifyerror=verifyerror,user=username,email=email)    
        # if no error occur go to welcome page
        else:
            return render_template('welcome.html',username=username)
        
    # if a get request is sent to index or '/' 
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)    