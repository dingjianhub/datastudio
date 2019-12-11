import qieman_index
import north_money



def main():
    print("[info]: =====正在获取指数估值数据.=====")
    qieman_index.run_qieman()
    print("[info]: =====正在获取北向资金.=====")
    north_money.run_north_money()

if __name__ == '__main__':
    main()
