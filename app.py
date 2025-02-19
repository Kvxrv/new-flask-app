from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure "index.html" exists inside "templates"

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is the about page.</p>"

@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1><p>Get in touch with us.</p>"

if __name__ == "__main__":
    app.run(debug=True)
