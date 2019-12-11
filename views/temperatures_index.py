from flask import Blueprint, jsonify, request

import pandas as pd
import os

from utils import response_code

temperature_index_bp = Blueprint("temperature_index_bp", __name__, url_prefix="/temperature")

@temperature_index_bp.route("/sh-index")
def SHIndex():
    """上证指数走势"""
    filename="/home/ay/workspace/datastudio/datas/北向资金流向.xlsx"
    data_list, date = read_north_money_data(filename, sheet_name="沪股通", col_name="上证指数")
    # print(data_list)
    response_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功",
        "date": date,
        "data_list": data_list
    }
    return jsonify(response_dict)
@temperature_index_bp.route("/sz-index")
def SZIndex():
    """深证成指走势"""
    filename="/home/ay/workspace/datastudio/datas/北向资金流向.xlsx"
    data_list, date = read_north_money_data(filename, sheet_name="深股通", col_name="深证指数")
    
    response_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功",
        "date": date,
        "data_list": data_list
    }
    return jsonify(response_dict)

@temperature_index_bp.route("/investors")
def change_investors():
    """新增投资者数量"""
    filename = "/home/ay/workspace/datastudio/datas/市场温度计.xlsx"
    sheet_name = "新增投资者"
    df = pd.read_excel(filename, sheet_name=sheet_name)
    date = df["日期"].to_list()
    data_list = df["新增投资者数(万)"].to_list()
    response_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功",
        "date": date,
        "data_list": data_list
    }
    return jsonify(response_dict)

@temperature_index_bp.route("/a-shares-values")
def ASharesValues():
    filename = "/home/ay/workspace/datastudio/datas/市场温度计.xlsx"
    sheet_name = "流通市值"
    df = pd.read_excel(filename, sheet_name=sheet_name)
    date = df["月份"].to_list()
    data_list = df["已上市流通市值(亿元)"].to_list()
    response_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功",
        "date": date,
        "data_list": data_list
    }
    return jsonify(response_dict)


@temperature_index_bp.route("/north-money")
def total_north_money():
    """北向资金的流入流出情况"""
    filename = "北向资金流向.xlsx"
    basedir = os.path.join(os.path.dirname(__file__), "../datas")
    filename = os.path.join(basedir, filename)
    market_type = request.args.get("market")
    response_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功", 
    }
    sh_data_list, sh_dates = read_north_money_data(filename, sheet_name="沪股通")
    sz_data_list, sz_dates = read_north_money_data(filename, sheet_name="深股通")
    cnts = len(sh_data_list) - len(sz_data_list)
    if market_type == "sh":
        response_dict.update({"date": sh_dates, "data_list": sh_data_list})
        return jsonify(response_dict)
    elif market_type == "sz":
        response_dict.update({"date": sz_dates, "data_list": sz_data_list})
        return jsonify(response_dict)
    else:
        totals = []
        j = 0
        for i in range(len(sh_data_list)):
            if i < cnts:
                totals.append(int(sh_data_list[i]))
            else:
                totals.append(int(sh_data_list[i] + sz_data_list[j]))
                j+=1
        # print(totals)
        response_dict.update({"date": sh_dates, "data_list": totals})
        return jsonify(response_dict)

@temperature_index_bp.route("/market-volumes")
def market_volumes():
    """统计沪深两市的成交量"""
    
    sh_data_list, date_list = read_sh_sz_market_volumes("上证指数")
    sz_data_list, date_list = read_sh_sz_market_volumes("深证成指")
    total_volumes = []
    for i in range(len(sz_data_list)):
        total_volumes.append(sh_data_list[i] + sz_data_list[i])

    response_dict = {
        "errno":response_code.success, 
        "errmsg":"获取成功", 
    }
    response_dict.update({
        "date": date_list,
        "sh_data_list":sh_data_list,
        "sz_data_list":sz_data_list,
        "total_volumes":total_volumes
    })
    return jsonify(response_dict)

def read_sh_sz_market_volumes(index_name):
    """读取沪深两市的成交量"""
    filename = f"datas/{index_name}.csv"
    df = pd.read_csv(filename, encoding="GBK")
    # print(df)
    try:
        data_list = df["成交额"].to_list()
    except Exception as e:
        data_list = df["成交额(亿元)"].to_list()
    date_list = df["日期"].to_list()
    results = []
    for item in data_list:
        # print(float(item.split("亿")[0]))
        if isinstance(item, str):
            results.append(float(item.split("亿")[0]))
    return results, date_list

def read_north_money_data(filename, sheet_name, col_name="资金流入"):
    """读取北向资金流入和对应指数涨跌幅数据"""
    
    df = pd.read_excel(filename, sheet_name=sheet_name)
    # df['日期'] = pd.to_datetime(df['日期'])
    df.sort_values('日期', inplace=True)
    date_list = df["日期"].to_list()
    # print(date_list)
    money_details = df[col_name].to_list()
    data_list = []
    for item in money_details:
        # print("type(item):", type(item))
        if isinstance(item, str):
            data_list.append(float(item.split("亿")[0]))
        else:
            data_list.append(item)
    return data_list, date_list