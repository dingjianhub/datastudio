from flask import Blueprint, redirect, jsonify
import pandas as pd


index_info_bp = Blueprint("index_info_bp", __name__, url_prefix="/index")


@index_info_bp.route("/<string:index_code>/pe")
def index_pe_value(index_code):
    """获取指数当前的PE"""
    col_name = "当前PE"
    read_flag, date_list, pe_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=601, errmsg="指数代码输入错误")

    return jsonify(errno=0, errmsg="获取成功", date=date_list, price=pe_list)


@index_info_bp.route("/<string:index_code>/price")
def index_price(index_code):
    """获取指数的价格"""
    col_name = "收盘价"
    read_flag, date_list, price_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=601, errmsg="指数代码输入错误")

    return jsonify(errno=0, errmsg="获取成功", date=date_list, price=price_list)


def read_datas(index_code, col_name):
    """读取DataFrame中特定列"""

    index_name = convert_index_code_to_name(index_code)
    if not check_index_code(index_name):
        return False, None, None

    filename = f"datas/{index_name}.csv"
    dataframe = pd.read_csv(filename, encoding='gbk')
    date_list = dataframe["日期"].tolist()
    price_list = dataframe[col_name].to_list()
    return True, date_list, price_list


def check_index_code(index_name):
    """判断指数名称是否正确"""
    if index_name is None:
        return False
    return True


def convert_index_code_to_name(index_code):
    """把指数代码转成指数名称"""
    index_name_code_dict = {
        "000016": "上证50",
        "000903": "中证100",
        "399330": "深证100",
        "000300": "沪深300",
        "000905": "中证500",
        "000852": "中证1000",
        "399006": "创业板指",
        "399005": "中小板指",
        "000932": "中证消费",
        "000991": "全指医药",
        "399812": "养老产业",
        "399986": "中证银行",
        "399975": "证券公司",
        "000993": "全指信息",
        "399971": "中证传媒",
        "000989": "全指可选",
        "000827": "中证环保",
        "399967": "中证军工"
    }
    code_list = index_name_code_dict.keys()
    if index_code not in code_list:
        print("请输入正确的指数代码")
        return None
    return index_name_code_dict[index_code]
