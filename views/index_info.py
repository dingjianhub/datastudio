from flask import Blueprint
import pandas as pd
import json

index_info_bp = Blueprint("index_info_bp", __name__, url_prefix="/index")


@index_info_bp.route("/<string:index_code>")
def index_pe_value(index_code):
    """展示指数当前的PE"""
    filename = r"datas/中证500.csv"
    dataframe = pd.read_csv(filename, encoding='gbk')
    date_list = dataframe["日期"].tolist()
    pe_list = dataframe["当前PE"].tolist()
    data = {"date": date_list, "pe": pe_list}

    return json.dumps(data)