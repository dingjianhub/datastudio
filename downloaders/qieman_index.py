import os
import time
import requests
import json
import csv
import sys
import pandas as pd

sys.path.append("/home/ay/workspace/datastudio")


from utils.common_config import Config


pd.set_option("expand_frame_repr", False)


class IndexValuation(object):
    def __init__(self):
        self.url = "https://qieman.com/pmdj/v2/idx-eval/latest"
        self.sina_url = r"https://hq.sinajs.cn/list=%s"
        self.current_date = None
        self.base_dir = r"/home/ay/workspace/datastudio/datas"

    def download_qieman(self):
        sign = Config().get_sign()
        headers = {
            'Accept': "application/json",
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Host': 'qieman.com',
            'Referer': 'https://qieman.com/idx-eval',
            "x-sign": sign,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }
        try:
            res = requests.get(self.url, headers=headers)
            data = json.loads(res.content.decode())
        except Exception as e:
            print("[error]: json error:", e)
            return None
        return data

    def download_sina(self, index_code):
        lower_index_code = index_code.lower()
        headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Referer": "https://finance.sina.com.cn/realstock/company/%s/nc.shtml" % lower_index_code,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                                    Chrome/75.0.3770.100 Safari/537.36"
        }
        hq_url = self.sina_url % lower_index_code
        try:
            res = requests.get(hq_url, headers=headers)
            if res.status_code == 200:
                index_data_str = res.content.decode(encoding="GBK")
            else:
                print("[error]: 请求失败")
                index_data_str = None
        except Exception as e:
            print("[error]: json error:", e)
            return None
        return index_data_str

    def change_index_code(self, index_name_code_dict):

        index_name = list(index_name_code_dict.keys())[-1]
        index_code = list(index_name_code_dict.values())[-1]

        if "." in index_code:
            index_code_split = index_code.split(".")
            index_code = index_code_split[-1] + index_code_split[0]

        error_index_name_list = ["证券公司", "中证银行"]
        for err_index_name in error_index_name_list:
            if index_name == err_index_name:
                index_code = index_code.replace("CSI", "SZ")

        return index_code

    def _forge_sh_index(self, data):
        if not data:
            print("[error]: _forge_sh_index() 从且慢获取指数估值失败.")
            return None
        stocks = data["idxEvalList"]
        sh_index_dict = {}
        sh_index_dict["indexName"] = "上证指数"
        sh_index_dict["indexCode"] = "000001.SH"
        sh_index_dict["pe"] = 0
        sh_index_dict["pb"] = 0
        sh_index_dict["peHigh"] = 0
        sh_index_dict["peLow"] = 0
        sh_index_dict["pePercentile"] = 0
        sh_index_dict["pbHigh"] = 0
        sh_index_dict["pbLow"] = 0
        sh_index_dict["pbPercentile"] = 0
        sh_index_dict["roe"] = 0
        sh_index_dict["scale"] = 0
        sh_index_dict["group"] = ""
        stocks.append(sh_index_dict)
        return stocks

    def parse_qieman_data(self, data):
        if not data:
            print("[error]: parse_qieman_data(data) data is None")
            return
        # 获取当前日期
        time_stamp = str(data["date"])[:10]
        time_array = time.localtime(int(time_stamp))
        self.current_date = time.strftime("%Y-%m-%d", time_array)
        # 获取指数
        stocks = self._forge_sh_index(data)
        return stocks

    def parse_sina_data(self, sina_data_str):
        valid_hq_str_len = 40
        data_str_len = len(sina_data_str)
        if data_str_len < valid_hq_str_len:
            print("[error]: 没有获取该指数的行情数据")
            return
        hq_str_list = []
        hq_str = sina_data_str.split("=")[-1].split(",")
        index_name = hq_str[0].split('"')[-1]
        open_price = hq_str[1]
        yesterday_close_price = hq_str[2]
        today_close_price = hq_str[3]
        max_price = hq_str[4]
        min_price = hq_str[5]
        amount = hq_str[9]
        date = hq_str[-3]

        hq_str_list.append(date)
        hq_str_list.append(index_name)
        hq_str_list.append(yesterday_close_price)
        hq_str_list.append(today_close_price)
        hq_str_list.append(amount)
        hq_str_list.append(open_price)
        hq_str_list.append(max_price)
        hq_str_list.append(min_price)

        return hq_str_list

    def get_sina_data(self, hq_str_list):
        if not hq_str_list:
            print("[error]: get_sina_data(): hq_str_list is none")
            return {}

        yesterday_close_price = float(hq_str_list[2])
        today_close_price = float(hq_str_list[3])
        amount = str(float(hq_str_list[4]) / 10 ** 8)[:7] + "亿元"
        change_point = str((today_close_price - yesterday_close_price))[0:6]
        change_ratio = str((float(change_point) / yesterday_close_price) * 100)[:6] + "%"
        open_price = hq_str_list[-3]
        max_price = hq_str_list[-2]
        min_price = hq_str_list[-1]

        hq_dict = {
            "成交额": amount,
            "涨跌量": change_point,
            "涨跌幅": change_ratio,
            "收盘价": today_close_price,
            "开盘价": open_price,
            "最高价": max_price,
            "最低价": min_price
        }
        return hq_dict

    def _create_series(self, stock):
        # print(stock)
        series_dict = {}
        index_name = stock["indexName"]
        if index_name == "可选消费":
            index_name = "全指可选"
        series_dict["日期"] = self.current_date
        series_dict["indexName"] = index_name
        series_dict["indexCode"] = stock["indexCode"]
        series_dict["pe"] = stock["pe"]
        cur_pb = stock["pb"]
        series_dict["pb"] = cur_pb
        series_dict["peHigh"] = stock["peHigh"]
        series_dict["peLow"] = stock["peLow"]
        pe_percentile = str(stock["pePercentile"] * 100)[:5] + "%" if stock["pePercentile"] else ""
        series_dict["pePercentile"] = pe_percentile
        pb_high = stock["pbHigh"]
        series_dict["pbHigh"] = pb_high
        series_dict["pbLow"] = stock["pbLow"]
        pb_percentile = str(stock["pbPercentile"] * 100)[:5] + "%" if stock["pbPercentile"] else ""
        series_dict["pbPercentile"] = pb_percentile
        series_dict["roe"] = str(stock["roe"] * 100)[:5] + "%"
        try:
            series_dict["scale"] = "%0.4f" % (pb_high / cur_pb)
        except Exception as e:
            series_dict["scale"] = 0
        series_dict["group"] = stock["group"]
        return series_dict

    def _create_dict(self, series_dict):
        if series_dict is None:
            print("[error]: series dict is None")
            exit(-1)
        index_name_col = []
        index_code_col = []
        pe_col = []
        pb_col = []
        pe_high_col = []
        pe_low_col = []
        pe_percentile_col = []
        pb_high_col = []
        pb_low_col = []
        pb_percentile_col = []
        roe_col = []
        pb_scale_col = []
        group_list = []
        current_date_col = []

        index_name_col.append(series_dict["indexName"])
        index_code_col.append(series_dict["indexCode"])
        pe_col.append(series_dict["pe"])
        pb_col.append(series_dict["pb"])
        pe_high_col.append(series_dict["peHigh"])
        pe_low_col.append(series_dict["peLow"])
        pe_percentile_col.append(series_dict["pePercentile"])
        pb_high_col.append(series_dict["pbHigh"])
        pb_low_col.append(series_dict["pbLow"])
        pb_percentile_col.append(series_dict["pbPercentile"])
        roe_col.append(series_dict["roe"])
        pb_scale_col.append(series_dict["scale"])
        group_list.append(series_dict["group"])

        current_date_col.append(self.current_date)
        index_dict = {
            "日期": current_date_col,
            "指数名称": index_name_col,
            "指数代码": index_code_col,
            "当前PE": pe_col,
            "当前PB": pb_col,
            "最高PE": pe_high_col,
            "最低PE": pe_low_col,
            "PE百分位": pe_percentile_col,
            "最高PB": pb_high_col,
            "最低PB": pb_low_col,
            "PB百分位": pb_percentile_col,
            "ROE": roe_col,
            "当前PB倍数": pb_scale_col,
            "指数位置": group_list,
        }
        return index_dict

    def _writer_csv_col(self, file_path):
        cols = ["日期", "指数名称", "指数代码", "当前PE", "当前PB", "最高PE", "最低PE",
                "PE百分位", "最高PB", "最低PB", "PB百分位", "ROE", "当前PB倍数", "分组",
                "成交额", "涨跌量", "涨跌幅", "收盘价", "开盘价", "最高价", "最低价"]
        df=pd.read_csv(file_path, encoding="GBK")
        last_date = df["日期"].to_list()[-2]
        if last_date is not "":
            return
        index_name = os.path.basename(file_path).split(".")[0]
        header = []
        try:
            f = open(file_path)
            csv_reader = csv.reader(f)
            header = next(csv_reader)
            # print(header)
        except Exception as e:
            pass
        f = open(file_path, "a", encoding="GBK", newline='')
        if "日期" in header:
            f.close()
            return
        csv_writer = csv.writer(f)
        csv_writer.writerow(cols)
        f.close()
        print(f"[info]: 写入'{index_name}'的列名称成功.")

    def _write_csv_rows(self, file_path, rows):
        if not rows:
            print("[error]: _write_csv_rows(): rows为None")
            return
        index_name = os.path.basename(file_path).split(".")[0]
        f = open(file_path, encoding="GBK")
        csv_reader = csv.reader(f)
        _ = next(csv_reader)
        latest_row = [-1]
        for row in csv_reader:
            latest_row = row
        latest_date = latest_row[0]
        if latest_date == self.current_date:
            print("[info]: 当前数据已是最新的.")
            return
        f = open(file_path, "a", encoding="GBK", newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow(rows)
        f.close()
        print(f"[info]: '{index_name}'的数据更新完成.")

    def save_to_csv(self, stocks):
        if not stocks:
            print("[error]: save_to_execl(): stocks is None")
            return

        for stock in stocks:
            index_name_code_dict = {}
            series_dict = self._create_series(stock)
            index_name = series_dict.get("indexName")
            old_index_code = series_dict.get("indexCode")
            index_name_code_dict[index_name] = old_index_code
            index_code = self.change_index_code(index_name_code_dict)
            sina_data_str = self.download_sina(index_code)
            hq_str_list = self.parse_sina_data(sina_data_str)
            hq_dict = self.get_sina_data(hq_str_list)
            rows = list(series_dict.values()) + list(hq_dict.values())
            file_path = os.path.join(self.base_dir, f"{index_name}.csv")
            self._writer_csv_col(file_path)
            self._write_csv_rows(file_path, rows)
            time.sleep(1)

    def save_index_group(self, group_filename, stocks, index_group_list):
        """把指数按照估值分组"""
        if not stocks:
            print("[error]: stocks is None")
            return

        low_key = index_group_list[0]
        mid_key = index_group_list[1]
        high_key = index_group_list[2]
        low_name_index_list = []
        mid_name_index_list = []
        high_name_index_list = []

        low_code_index_list = []
        mid_code_index_list = []
        high_code_index_list = []
        c = []
        date_list = [self.current_date]
        for stock in stocks:
            group = stock["group"]
            if "可选消费" == stock["indexName"]:
                stock["indexName"] = "全指可选"
            if group == low_key:
                low_name_index_list.append(stock["indexName"])
                low_code_index_list.append(stock["indexCode"])
            elif group == mid_key:
                mid_name_index_list.append(stock["indexName"])
                mid_code_index_list.append(stock["indexCode"])
            elif group == high_key:
                high_name_index_list.append(stock["indexName"])
                high_code_index_list.append(stock["indexCode"])

        low_dataframe = pd.DataFrame({
            "日期": date_list * len(low_name_index_list),
            "指数代码": low_code_index_list,
            "指数名称": low_name_index_list
        })
        mid_dataframe = pd.DataFrame({
            "日期": date_list * len(mid_name_index_list),
            "指数代码": mid_code_index_list,
            "指数名称": mid_name_index_list
        })
        high_dataframe = pd.DataFrame({
            "日期": date_list * len(high_name_index_list),
            "指数代码": high_code_index_list,
            "指数名称": high_name_index_list
        })

        excel_writer = pd.ExcelWriter(group_filename, engine='openpyxl')
        low_dataframe.to_excel(excel_writer, sheet_name="低估指数", index=False)
        mid_dataframe.to_excel(excel_writer, sheet_name="估值适中", index=False)
        high_dataframe.to_excel(excel_writer, sheet_name="高估指数", index=False)
        excel_writer.save()
        print("[info]: 指数分组成功!")


def run_qieman():
    group_filename = os.path.join(
        r"/home/ay/workspace/datastudio/datas","指数分组.xlsx")
    index_group_list = ["LOW", "MID", "HIGH"]
    data_writer = IndexValuation()
    data_dict = data_writer.download_qieman()
    stocks = data_writer.parse_qieman_data(data_dict)
    data_writer.save_to_csv(stocks)
    data_writer.save_index_group(group_filename, stocks, index_group_list)
    print("[info]: 指数信息已全部更新完成")


if __name__ == "__main__":
    run_qieman()

