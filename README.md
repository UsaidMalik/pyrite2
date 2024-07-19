# About

Created for CS4CS 2024 to teach students about phishing and social engineering

# How To Use

Install flask in a virtual environment, activate the venv, run python app.py in the venv the app is now hosted on your machines IP address. In the browser type in your machines IP address on the network and enter some username and password, it will be saved locally to a file called usernames_and_passwords.txt a lock is there to prevent race conditions in writing. Views stores the login and password page shown it can be changed to whatever. After submitting the form redirects to the homepage of NYU to prevent any suspicion. Done on HTTP without a certificate for HTTPS, to make it more convincing a cert could theoretically be purchased & added. 

# Warnings & Disclaimers

**DO NOT USE TO ACTUALLY PHISH**, this will probably not work to phish anyone but do not try. **FOR EDUCATIONAL PURPOSES ONLY** We take no responsibility for you doing
something illegal
