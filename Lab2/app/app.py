from flask import Flask, render_template, request
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Initialize Flask-BasicAuth
basic_auth = BasicAuth(app)

# Define allowed users and their passwords
app.config['BASIC_AUTH_USERNAME'] = 'user1'
app.config['BASIC_AUTH_PASSWORD'] = 'password1'

@app.route('/')
def home():
    return render_template('home.html')

# Protect the data_entry route with basic authentication
@app.route('/data_entry')
@basic_auth.required
def data_entry():
    return render_template('data_entry.html')

if __name__ == '__main__':
    app.run()
