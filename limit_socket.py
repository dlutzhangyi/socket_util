import tushare as ts
import time
import numpy as np
from math import isnan

# 获取a股的所有股票数据
def get_socket_data():
    socket_data = ts.get_stock_basics()
    socket_dict = {}

    for index, row in socket_data.iterrows():
        # print(index,row['name'])  # 输出每行的索引值
        if row['name'].find("ST") == -1:
            socket_dict[index]=row['name']
    return socket_dict

# 获取某个股票的历史数据
def get_socket_hist_data(socket_number):
    return ts.get_hist_data(socket_number)

# 获取某个股票近10天内的涨停次数，需要从今天开始往前数，连续涨停
def get_socket_limit_number(socket_number):
    data = get_socket_hist_data(socket_number)
    limit_number = 0
    default_length = 10
    if len(data["p_change"].values) < 10:
        default_length = len(data["p_change"].values) 
    for i in range(default_length):
        if data["p_change"].values[i]>= 9.9:
            limit_number = limit_number + 1
        else:
            break
    return limit_number

# 获取a股所有上市的涨停板列表
def get_limit_socket_data(sockets_dict):
    for key in sockets_dict:
        number = get_socket_limit_number(key)
        if number >= 2:
            print("股票代码:",key,"股票名:",sockets_dict[key],"涨停次数:",number)

if __name__ == "__main__":
    all_sockets = get_socket_data()
    get_limit_socket_data(all_sockets)
    # number = get_socket_limit_number("300318") 
    # print(number)
    # print(get_socket_data())
    # print(get_socket_hist_data("300318"))
