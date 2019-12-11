import csv
import os
import time
import sys

import demjson
import requests
import pandas as pd

sys.path.append("/home/ay/workspace/datastudio")

from utils.common_config import Config
from utils import sheet_add


class NorthwardMoney(object):
    def __init__(self):
        self.base_url = r"http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get"
        self.base_dir = r"/home/ay/workspace/datastudio/datas"

    def download_history_data(self, exchange_type, market_type):
        headers = {
            "Referer": "http://data.eastmoney.com/hsgt/index.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/74.0.3729.169 Safari/537.36",
        }

        token = Config().get_token()
        query_data = {
            "type": exchange_type,
            "token": token,
            "filter": "(MarketType=%s)" % market_type,
            "sr": -1,
            "st": "DetailDate",
        }

        try:
            res = requests.get(self.base_url, headers=headers, params=query_data)
            data = res.content.decode()
        except Exception as e:
            print("[error]: download_history_data():获取北向资金历史失败:", e)
            return None
        return data

    def download_stock_data(self, stock_type, market_type):
        headers = {
            "Referer": "http://data.eastmoney.com/hsgt/index.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                                    Chrome/74.0.3729.169 Safari/537.36",
        }

        token = Config().get_token()
        query_data = {
            "type": stock_type,
            "token": token,
            "filter": "(MarketType=%s)" % market_type,
            "sr": -1,
            "st": "DetailDate, Rank",
            "ps": 10,
        }

        try:
            res = requests.get(self.base_url, headers=headers, params=query_data)
            stocks_data = res.content.decode()
        except Exception as e:
            print("[error]: download_stock_data()获取前十大成交股失败:", e)
            return None
        return stocks_data

    def parse_data(self, datas):
        try:
            dict_obj = demjson.decode(datas.split("=")[-1])
        except Exception as e:
                return None
        return dict_obj

    def save_header(self):
        hgt_filename = os.path.join(self.base_dir, "沪股通.csv")
        sgt_filename = os.path.join(self.base_dir, "深股通.csv")
        hgt_cols = ["日期", "资金流入", "上证指数", "涨跌幅"]
        sgt_cols = ["日期", "资金流入", "深证指数", "涨跌幅"]
        with open(hgt_filename, 'w', encoding="GBK") as f:
            writer = csv.writer(f)
            writer.writerow(hgt_cols)
        with open(sgt_filename, 'w', encoding="GBK") as f:
            writer = csv.writer(f)
            writer.writerow(sgt_cols)

    def save_data(self):
        filename = os.path.join(self.base_dir,"北向资金流向.xlsx")
        excel_writer = pd.ExcelWriter(filename)
        pages = 30
        datas = None
        market_type_list = [1, 3]
        for market_type in market_type_list:
            page_index = 1
            while page_index <= pages:
                if market_type == 1:
                    print("[info]: 正在请求'沪股通'第%d页数据" % page_index)
                    datas = self.parse_data(market_type=market_type, page_index=page_index)
                elif market_type == 3:
                    print("[info]: 正在请求'深股通'第%d页数据" % page_index)
                    datas = self.parse_data(market_type=market_type, page_index=page_index)
                if not datas:
                    print("[error]: save_data():data is None，保存失败！")
                    return
                if market_type == 1:
                    print("[info]: 正在保存'沪股通'第%d页数据" % page_index)
                    filename = "沪股通.csv"
                    self._save_rows(datas, filename)
                    # sheet_name = "沪股通"
                    # self._save_to_excel(excel_writer, datas, sheet_name)
                    # break
                elif market_type == 3:
                    print("[info]: 正在保存'沪股通'第%d页数据" % page_index)
                    filename = "深股通.csv"
                    self._save_rows(datas, filename)
                    # sheet_name = "深股通"
                    # self._save_to_excel(excel_writer, datas, sheet_name)
                    # break

                page_index += 1
                time.sleep(1)
            excel_writer.save()

        print("[info]: 全部数据更新完成")

    def _save_rows(self, datas, filename):
        full_filename = os.path.join(self.base_dir, filename)
        origin_df = pd.read_csv(full_filename, nrows=1, encoding="GBK")
        origin_latest_date = origin_df["日期"].tolist()[-1]

        for item in datas:
            date = item.get("DetailDate").split("T")[0]
            inflows_money = str(item.get("DRZJLR") / 100)[0:5] + "亿元"
            index_point = item.get("SSEChange")
            index_percent = str(item.get("SSEChangePrecent") * 100)[0:4] + "%"

            with open(full_filename, "a", encoding="GBK") as f:
                writer = csv.writer(f)
                writer.writerow([date, inflows_money, index_point, index_percent])

    def merge_to_excel(self):
        csv_file_list = []
        for root_dir, _, files in os.walk(self.base_dir):
            for file in files:
                if file.endswith(".csv"):
                    csv_file_list.append(os.path.join(root_dir, file))

        excel_filename = filename = os.path.join(self.base_dir,"北向资金流向.xlsx")
        excel_writer = pd.ExcelWriter(excel_filename)
        for csv_file in csv_file_list:
            index_name = os.path.basename(csv_file).split(".")[0]
            df = pd.read_csv(csv_file, encoding="GBK")
            df.to_excel(excel_writer, sheet_name=index_name, index=False)
        print("[info]: 合并到excel完成！")
        excel_writer.save()

    def _save_to_excel(self, excel_writer, datas, sheet_name):
        # print(datas[0])
        first_data = datas[0]
        latest_date = first_data.get("DetailDate").split("T")[0]
        # print(latest_date)
        try:
            origin_df = pd.read_excel(excel_writer, sheet_name=sheet_name)
        except Exception as e:
            origin_df = pd.DataFrame()
        if not origin_df.empty:
            origin_latest_date = origin_df["日期"].tolist()[0]
            if latest_date == origin_latest_date:
                print("[info]: 源数据还未更新，稍后再试")
                return False
        date_list = []
        inflows_money_list = []
        index_point_list = []
        index_percent_list = []

        inflows_money = str(first_data.get("DRZJLR") / 100)[0:5] + "亿元"
        index_point = first_data.get("SSEChange")
        index_percent = str(first_data.get("SSEChangePrecent") * 100)[0:4] + "%"

        date_list.append(latest_date)
        inflows_money_list.append(inflows_money)
        index_point_list.append(index_point)
        index_percent_list.append(index_percent)

        if sheet_name == "沪股通":
            index_name = "上证指数"
        else:
            index_name = "深证指数"

        latest_dict = {
            "日期": date_list,
            "资金流入": inflows_money_list,
            index_name: index_point_list,
            "涨跌幅": index_percent_list
        }

        latest_df = pd.DataFrame(latest_dict)
        frames = [latest_df, origin_df]
        total_df = pd.concat(frames)
        total_df.to_excel(excel_writer, index=False, sheet_name=sheet_name)
        print("[info]: 保存%s数据成功" % sheet_name)

    def get_hgt_total_data(self, exchange_type):
        hgt_total_data_list = []
        market_type = 1
        is_received = True
        while is_received:
            print("[info]: 正在整理'沪股通'的数据")
            datas = self.download_history_data(exchange_type, market_type)
            dict_obj_list = self.parse_data(datas)
            if not dict_obj_list:
                print("[error]: get_hgt_total_data():解析'沪股通'数据出错!")
                return None
            for item in dict_obj_list:
                hgt_total_data_list.append(item)
            is_received = False
        print("[info]: 解析'沪股通'数据完成")
        return hgt_total_data_list

    def get_sgt_total_data(self, exchange_type):
        sgt_total_data_list = []
        market_type = 3
        is_received = True
        while is_received:
            print("[info]: 正在整理'深股通'的数据")
            datas = self.download_history_data(exchange_type, market_type)
            dict_obj_list = self.parse_data(datas)
            if not dict_obj_list:
                print("[error]: get_sgt_total_data():解析'深股通'数据出错!")
                return None
            for item in dict_obj_list:
                sgt_total_data_list.append(item)
            time.sleep(1)
            is_received = False
        print("[info]: 解析'深股通'数据完成")
        return sgt_total_data_list

    def get_hgt_top_10_stocks(self, stock_type):
        hgt_stock_top_10_list = []
        market_type = 1
        stock_name = "沪股通前10大成交股"
        print("[info]: 正在整理'%s'数据" % stock_name)
        datas = self.download_stock_data(stock_type, market_type)
        dict_obj_list = self.parse_data(datas)
        if not dict_obj_list:
            print("[error]: get_hgt_top_10_stocks():整理'%s'数据出错" % stock_name)
            return None
        for item in dict_obj_list:
            hgt_stock_top_10_list.append(item)
        print("[info]: 整理'%s'数据完成" % stock_name)
        return hgt_stock_top_10_list

    def get_sgt_top_10_stocks(self, stock_type):
        sgt_stock_top_10_list = []
        market_type = 3
        stock_name = "深股通前10大成交股"
        print("[info]: 正在整理'%s'数据" % stock_name)
        datas = self.download_stock_data(stock_type, market_type)
        dict_obj_list = self.parse_data(datas)
        if not dict_obj_list:
            print("[error]: get_sgt_top_10_stocks():整理'%s'数据出错" % stock_name)
            return None
        for item in dict_obj_list:
            sgt_stock_top_10_list.append(item)
        print("[info]: 整理'%s'数据完毕" % stock_name)
        return sgt_stock_top_10_list

    def save_hgu_to_excel(self, excel_writer, hgt_total_dict_data_list):
        if not hgt_total_dict_data_list:
            print("[error]: save_hgu_to_excel():沪股通数据为空")
            return
        date_list = []
        inflows_money_list = []
        index_point_list = []
        index_percent_list = []
        for data in hgt_total_dict_data_list:
            date = data.get("DetailDate").split("T")[0]
            inflows_money = str(data.get("DRZJLR") / 100)[0:5] + "亿元"
            index_point = data.get("SSEChange")
            index_percent = str(data.get("SSEChangePrecent") * 100)[0:4] + "%"

            date_list.append(date)
            inflows_money_list.append(inflows_money)
            index_point_list.append(index_point)
            index_percent_list.append(index_percent)

        hgt_dict = {
            "日期": date_list,
            "资金流入": inflows_money_list,
            "上证指数": index_point_list,
            "涨跌幅": index_percent_list
        }
        hgt_df = pd.DataFrame(hgt_dict)
        hgt_df.to_excel(excel_writer, sheet_name="沪股通", index=False)
        print("[info]: 沪股通数据保存成功!")

    def save_sgu_to_excel(self, excel_writer, sgt_total_dict_data_list):
        if not sgt_total_dict_data_list:
            print("[error]: save_sgu_to_excel():深股通数据为空")
            return
        date_list = []
        inflows_money_list = []
        index_point_list = []
        index_percent_list = []
        for data in sgt_total_dict_data_list:
            date = data.get("DetailDate").split("T")[0]
            inflows_money = str(data.get("DRZJLR") / 100)[0:5] + "亿元"
            index_point = data.get("SSEChange")
            index_percent = str(data.get("SSEChangePrecent") * 100)[0:4] + "%"

            date_list.append(date)
            inflows_money_list.append(inflows_money)
            index_point_list.append(index_point)
            index_percent_list.append(index_percent)

        hgt_dict = {
            "日期": date_list,
            "资金流入": inflows_money_list,
            "深证指数": index_point_list,
            "涨跌幅": index_percent_list
        }
        hgt_df = pd.DataFrame(hgt_dict)
        hgt_df.to_excel(excel_writer, sheet_name="深股通", index=False)
        print("[info]: 深股通数据保存成功!")

    def save_shares_to_excel(self, excel_writer, stock_list):
        if not stock_list:
            print("[error]: save_shares_to_excel():前十大成交股数据为空")
            return
        date_list = []
        rank_list = []
        share_code_list = []
        share_name_list = []
        share_close_price_list = []
        share_change_percent_list = []
        amount_list = []

        for data in stock_list:
            # print(data)
            date = data.get("DetailDate").split("T")[0]
            rank = data.get("Rank")
            share_code = data.get("Code")
            share_name = data.get("Name")
            share_close = data.get("Close")
            share_percent = str(data.get("ChangePercent"))[0:4] + "%"
            market_type = data.get("MarketType")
            if int(market_type) == 1:
                # amount = self._set_amount(str(data.get("HGTJME")))
                amount = str(data.get("HGTJME")) + "元"
            else:
                amount = str(data.get("SGTJME")) + "元"

            date_list.append(date)
            rank_list.append(rank)
            share_code_list.append(share_code)
            share_name_list.append(share_name)
            share_close_price_list.append(share_close)
            share_change_percent_list.append(share_percent)
            amount_list.append(amount)

        sheet_name = date_list[0]
        share_dict = {
            "日期": date_list,
            "排名": rank_list,
            "股票代码": share_code_list,
            "股票名称": share_name_list,
            "收盘价": share_close_price_list,
            "涨跌幅": share_change_percent_list,
            "净买入额": amount_list
        }
        share_dataframe = pd.DataFrame(share_dict)
        share_dataframe.sort_values(by=["排名"], inplace=True)
        # print(share_dataframe)
        sheet_add.excel_add_sheet(share_dataframe, excel_writer, sheet_name)


def run_north_money():
    exchange_type = "HSGTHIS"
    stock_type = "HSGTCJB"
    base_dir = r"/home/ay/workspace/datastudio/datas"
    filename = r"北向资金流向.xlsx"
    hgt_share_filename = os.path.join(base_dir, r"沪股通前十大成交股.xlsx")
    sgt_share_filename = os.path.join(base_dir, r"深股通前十大成交股.xlsx")
    full_filename = os.path.join(base_dir, filename)
    excel_writer = pd.ExcelWriter(full_filename)
    hgt_shares_excel_writer = pd.ExcelWriter(hgt_share_filename, engine='openpyxl')
    sgt_shares_excel_writer = pd.ExcelWriter(sgt_share_filename, engine='openpyxl')
    north_money = NorthwardMoney()
    # 统计北向资金的每日净买入/卖出额
    hgt_total_dict_data_list = north_money.get_hgt_total_data(exchange_type)
    sgt_total_dict_data_list = north_money.get_sgt_total_data(exchange_type)
    north_money.save_hgu_to_excel(excel_writer, hgt_total_dict_data_list)
    north_money.save_sgu_to_excel(excel_writer, sgt_total_dict_data_list)

    # 统计北向资金的前十大成交股
    hgt_top_10_shares = north_money.get_hgt_top_10_stocks(stock_type)
    sgt_top_10_shares = north_money.get_sgt_top_10_stocks(stock_type)
    north_money.save_shares_to_excel(hgt_shares_excel_writer, hgt_top_10_shares)
    north_money.save_shares_to_excel(sgt_shares_excel_writer, sgt_top_10_shares)

    hgt_shares_excel_writer.save()
    sgt_shares_excel_writer.save()
    excel_writer.save()
    print("[info]: 所有数据都已保存完毕!")


if __name__ == "__main__":
    run_north_money()
