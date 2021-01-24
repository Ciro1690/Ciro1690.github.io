from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message
from forms import ContactForm
import os

# use secret key in production or default to our dev one
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abc123')
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'Ciro16@gmail.com'  # enter your email here
app.config['MAIL_PASSWORD'] = SECRET_KEY # enter your password here

mail = Mail(app)
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/recent_work")
def recent_work():
    return render_template("recent_work.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/reach_out", methods=['GET', 'POST'])
def reach_out():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        msg = Message(f"Message from {name}", sender=f"{email}", recipients=['Ciro16@gmail.com'])
        msg.body = f"{message} from {email}"

        mail.send(msg)
        flash("Email sent", "success")
        return redirect('/')
    return render_template("reach_out.html", form=form)

