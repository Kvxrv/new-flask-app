from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My New Flask App!</h1>"

@app.route('/about')
def about():
    return "<h2>About Us</h2><p>This is a simple Flask app.</p>"

@app.route('/contact')
def contact():
    return "<h2>Contact Us</h2><p>Email us at support@example.com</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
