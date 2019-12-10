from flask import Blueprint, redirect, jsonify
import pandas as pd
import os

from utils import response_code



index_info_bp = Blueprint("index_info_bp", __name__, url_prefix="/index")

@index_info_bp.route("/group")
def index_groups():
    """指数分组"""
    data_files = os.listdir("/home/ay/workspace/datastudio/datas")
    low_index_list = [
            {"code":"000905", "name":"中证500"},
            {"code":"000016", "name":"上证50"},
            {"code":"000852", "name":"中证1000"},
            {"code":"399005", "name":"中小板指"},
            {"code":"000991", "name":"全指医药"},
            {"code":"399812", "name":"养老产业"},
            {"code":"399986", "name":"中证银行"},
            {"code":"000989", "name":"全指可选"},
            {"code":"000827", "name":"中证环保"},
            {"code":"399967", "name":"中证军工"}
        ]
    mid_index_list = [
            {"code":"399330", "name":"深证100"},
            {"code":"000903", "name":"中证100"},
            {"code":"000300", "name":"沪深300"},
            {"code":"399006", "name":"创业板指"},
            {"code":"399975", "name":"证券公司"},
            {"code":"000993", "name":"全指信息"},
        ]
    high_index_list = [
            {"code":"000932", "name":"中证消费"}
        ]
    results_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功",
        "lowIndex":low_index_list,
        "midIndex": mid_index_list,
        "highIndex": high_index_list
    }
    return jsonify(results_dict)

@index_info_bp.route("/<string:index_code>/pe")
def index_pe_value(index_code):
    """获取指数当前的PE"""
    col_name = "当前PE"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")

    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pe=data_list)

@index_info_bp.route("/<string:index_code>/pb")
def index_pb_value(index_code):
    col_name = "当前PB"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")

    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pb=data_list)


@index_info_bp.route("/<string:index_code>/price")
def index_price(index_code):
    """获取指数的价格"""
    col_name = "收盘价"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")

    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, price=data_list)

@index_info_bp.route("/<string:index_code>/roe")
def index_roe(index_code):
    """获取指数的价格"""
    col_name = "ROE"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, roe=data_list)


@index_info_bp.route("/<string:index_code>/pe-percent")
def index_pe_percent(index_code):
    """获取指数的价格"""
    col_name = "PE百分位"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pePercent=data_list)

@index_info_bp.route("/<string:index_code>/pb-percent")
def index_pb_percent(index_code):
    """获取指数的PB百分位"""
    col_name = "PB百分位"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pbPercent=data_list)

@index_info_bp.route("/<string:index_code>/change-percent")
def index_change_percent(index_code):
    """获取指数的PB百分位"""
    col_name = "涨跌幅"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, chPercent=data_list)

@index_info_bp.route("/<string:index_code>/volumes")
def index_total_volumes(index_code):
    """获取指数的PB百分位"""
    col_name = "成交额"
    read_flag, index_name, date_list, data_list = read_datas(index_code, col_name)
    if not read_flag:
        return jsonify(errno=response_code.invalid_index_code, errmsg="指数代码输入错误")
    # print(data_list)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, totalVolumes=data_list)

def read_datas(index_code, col_name):
    """读取DataFrame中特定列"""

    index_name = convert_index_code_to_name(index_code)
    if not check_index_code(index_name):
        return False, None, None, None

    filename = f"datas/{index_name}.csv"
    dataframe = pd.read_csv(filename, encoding='gbk')
    date_list = dataframe["日期"].tolist()
    target_list = dataframe[col_name].to_list()
    special_fields = ["ROE", "PE百分位", "PB百分位", "涨跌幅", "成交额"]
    if col_name in special_fields:
        special_list = []
        
        for item in target_list:
            if "%" in item:
                special_list.append(item.split("%")[0])
            elif "亿" in item:
                    special_list.append(item.split(".")[0])
        return True, index_name, date_list, special_list
    return True, index_name, date_list, target_list

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
    if index_code is None:
        return index_name_code_dict.values()
    return index_name_code_dict[index_code]


def check_index_code(index_name):
    """判断指数名称是否正确"""
    if index_name is None:
        return False
    return True