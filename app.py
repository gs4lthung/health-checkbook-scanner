# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
