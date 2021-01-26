from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message
from forms import ContactForm
import os

# use secret key in production or default to our dev one
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abc123')

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'Ciro16@gmail.com'  # enter your email here
app.config['MAIL_PASSWORD'] = os.environ.get('SECRET_KEY', 'abc123') # enter your password here

mail = Mail(app)
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/skills_education")
def skills_education():
    return render_template("skills_education.html")

@app.route("/recent_work")
def recent_work():
    return render_template("recent_work.html")


@app.route("/about_me")
def contact():
    return render_template("about_me.html")

@app.route("/contact", methods=['GET', 'POST'])
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
    return render_template("contact.html", form=form)

