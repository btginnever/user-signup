from flask import Flask, request, redirect
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    template = jinja_env.get_template('html_form.html')
    return template.render(user_name_error ='', email_error='', password_error='')
    
    

@app.route("/", methods=['POST'])
def is_valid():
    user_name= request.form['user_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email= request.form['email']
    user_name_not_populated = ""
    is_email_not_populated = email == ""
    is_email_valid = email.count('@')==1 and email.count('.')==1
    password_error = ''
    email_error= ''
    user_name_error = ''



    if not is_email_valid:
        email_error = 'not a valid email'

    if password != confirm_password:
        password_error = 'passwords do not match'
   
    if user_name_not_populated:
        user_name_error = "no username selected" 

    if not email_error and not password_error and not user_name_error:
        return "<h1> Welcome," + user_name + "</h1>"  

    else:
        template = jinja_env.get_template('html_form.html')
        return template.render(user_name_error= user_name_error, password_error=password_error,
email_error=email_error)




   


app.run()