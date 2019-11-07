from flask import Flask
from flask_cors import *

from views.index_info import index_info_bp


index_app = Flask(__name__)
# 解决跨域问题
CORS(index_app,  supports_credentials=True)
# 注册蓝图
index_app.register_blueprint(index_info_bp)


@index_app.route("/")
def index():
    return "Hello, DataStudio!"


if __name__ == '__main__':
    index_app.run(debug=True)