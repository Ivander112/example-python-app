from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/nama')
def hello_moder():
    return 'Di update oleh ivan'

@app.route('/secret')
def hello_secret():
    return 'gk ad secret'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port="4321")
