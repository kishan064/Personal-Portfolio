from flask import Flask,render_template,url_for
from contact import contact_data

app = Flask(__name__)

@app.route("/") 
@app.route("/home")  
def home():
    return render_template("home.html",title = "Home Page")

@app.route("/about")  
def about():
    return render_template("about.html",title = "About Page")

@app.route("/projects")  
def projects():
    return render_template("projects.html",title = "projects Page")

@app.route("/contact")
def contact():
     return render_template("contact.html",title = "contact Page",cont = contact_data)

if __name__ == "__main__":
    app.run(debug=True)