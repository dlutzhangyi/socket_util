import tushare as ts
import time


def get_socket_data():
    socket_data = ts.get_stock_basics()
    socket_dict = {}

    for index, row in socket_data.iterrows():
        # print(index,row['name'])  # 输出每行的索引值
        if row['name'].find("ST") == -1:
            socket_dict[index]=row['name']
    return socket_dict

def get_socket_hist_data(socket_number,day):
    data = ts.get_hist_data(socket_number)


if __name__ == "__main__":
    data = get_socket_data()
    print(data)
