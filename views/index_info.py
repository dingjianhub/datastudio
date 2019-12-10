from flask import Blueprint, redirect, jsonify
import pandas as pd
import os

from utils import response_code


index_info_bp = Blueprint("index_info_bp", __name__, url_prefix="/index")

@index_info_bp.route("/group")
def index_groups():
    """指数分组"""
    low_index_list = parse_index_group(read_index_group(index=0)[0], read_index_group(index=0)[1])
    mid_index_list = parse_index_group(read_index_group(index=1)[0], read_index_group(index=1)[1])
    high_index_list = parse_index_group(read_index_group(index=2)[0], read_index_group(index=2)[1])

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
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pe=data_list)

@index_info_bp.route("/<string:index_code>/pb")
def index_pb_value(index_code):
    """获取PB"""
    col_name = "当前PB"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pb=data_list)


@index_info_bp.route("/<string:index_code>/price")
def index_price(index_code):
    """获取价格"""
    col_name = "收盘价"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, price=data_list)

@index_info_bp.route("/<string:index_code>/roe")
def index_roe(index_code):
    """获取ROE"""
    col_name = "ROE"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, roe=data_list)

@index_info_bp.route("/<string:index_code>/pe-percent")
def index_pe_percent(index_code):
    """获取PE百分位"""
    col_name = "PE百分位"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pePercent=data_list)

@index_info_bp.route("/<string:index_code>/pb-percent")
def index_pb_percent(index_code):
    """获取PB百分位"""
    col_name = "PB百分位"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, pbPercent=data_list)

@index_info_bp.route("/<string:index_code>/change-percent")
def index_change_percent(index_code):
    """获取指数涨跌幅"""
    col_name = "涨跌幅"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, chPercent=data_list)

@index_info_bp.route("/<string:index_code>/volumes")
def index_total_volumes(index_code):
    """获取指数成交量"""
    col_name = "成交额"
    index_name, date_list, data_list = read_datas(index_code, col_name)
    return jsonify(errno=response_code.success, errmsg="获取成功", name=index_name, date=date_list, totalVolumes=data_list)

def read_datas(index_code, col_name):
    """读取DataFrame中特定列"""
    index_name = convert_index_code_to_name(index_code)
    if not check_index_code(index_name):
        return  None, None, None
    if index_name == "可选消费":
        index_name = "全指可选"
    filename = f"datas/{index_name}.csv"
    # print(filename)
    dataframe = pd.read_csv(filename, encoding='gbk', keep_default_na = False)
    target_list = dataframe[col_name].to_list()
    # print(target_list)
    zero_cnt = 0
    for item in target_list:
        if item == "":
            zero_cnt += 1
    date_list = dataframe["日期"].tolist()[zero_cnt:]
    if zero_cnt == len(target_list):
        target_list=None
    # print(target_list)
    if target_list is None:
        return index_name, date_list, None
    special_fields = ["ROE", "PE百分位", "PB百分位", "涨跌幅", "成交额"]
    if col_name in special_fields:
        special_list = []
        for item in target_list:
            if "%" in item:
                special_list.append(item.split("%")[0])
            elif "亿" in item:
                    special_list.append(item.split(".")[0])
        return index_name, date_list, special_list
    return index_name, date_list, target_list

def read_index_group(index=-1):
    """读取不同分组的指数"""
    group_filename= "/home/ay/workspace/datastudio/datas/指数分组.xlsx"
    sheet_names = pd.ExcelFile(group_filename).sheet_names
    if index == -1:
        """读取所有的指数"""
        index_codes = []
        index_names = []
        # print(len(sheet_names))
        for i in range (0, len(sheet_names)):
            index_codes += pd.read_excel(group_filename, sheet_name=sheet_names[i],encoding='gbk')["指数代码"].to_list()
            index_names += pd.read_excel(group_filename, sheet_name=sheet_names[i],encoding='gbk')["指数名称"].to_list()
        return index_codes, index_names
            
    index_codes = pd.read_excel(group_filename, sheet_name=sheet_names[index],encoding='gbk')["指数代码"].to_list()
    index_names = pd.read_excel(group_filename, sheet_name=sheet_names[index],encoding='gbk')["指数名称"].to_list()
    return index_codes, index_names
        

def parse_index_group(index_codes, index_names, all_index=0):
    """处理指数代码"""
    results = []
    if index_codes is None or index_names is None:
        print(f"{index_codes} or {index_names} is empty list.")
        return None
    all_index_dict = {}
    for code, name in zip(index_codes, index_names):
        item = {}
        new_code = code.split(".")[0]
        if new_code.isdigit():
            if all_index == 1:
                """不分组，返回所有格式化后的指数"""
                all_index_dict.update({new_code: name})
            item["code"] = new_code
            item["name"] = name
            results.append(item)

    if all_index == 1:
        return all_index_dict
    return results

def convert_index_code_to_name(index_code):
    """把指数代码转成指数名称"""
    index_codes, index_names = read_index_group()
    index_name_code_dict =parse_index_group(index_codes, index_names, all_index=1)
    # print(index_name_code_dict)
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