from flask import Flask, render_template
from flask_cors import *
import requests

from views.index_info import index_info_bp
from views.home import home_bp
from views.temperatures_index import temperature_index_bp


app = Flask(__name__, template_folder="./dist")
# 解决跨域问题
CORS(app,  supports_credentials=True)
# 注册蓝图
app.register_blueprint(index_info_bp)
app.register_blueprint(home_bp)
app.register_blueprint(temperature_index_bp)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     if app.debug:
#         print("path:",path)
#         return requests.get('http://localhost:8080/{}'.format(path)).text
#     print("path:",path)
#     return render_template("index.html")

# @app.route("/")
# def index():
#     return "Hello, DataStudio!"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
