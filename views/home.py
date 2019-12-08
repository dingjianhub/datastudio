import os

from flask import Blueprint, jsonify
from utils import response_code

home_bp = Blueprint("home_bp", __name__)

@home_bp.route("/search")
def search_all_index():
    data_files = os.listdir("D:\量化投资之路\workspace\datastudio\datas")
    results = []
    for filename in data_files:
        # print(filename)
        # return "hello"
        index_name = filename.split(".")[0]

        results.append(index_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", results=results)