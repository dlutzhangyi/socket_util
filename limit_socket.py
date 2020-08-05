import tushare as ts
import time
import csv
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
    try:
        if len(data["p_change"].values) < 10:
            default_length = len(data["p_change"].values) 
    except:
        print("获取p_change的values失败,股票代码为:",socket_number)        
    for i in range(default_length):
        if data["p_change"].values[i]>= 9.9:
            limit_number = limit_number + 1
        else:
            break
    return limit_number

# 获取a股所有上市的涨停板列表
def get_limit_socket_data(sockets_dict):
    today = time.strftime("%Y-%m-%d", time.localtime())
    file_name = "socket_limit_number_" + today +".csv"
    with open(file_name,'wb') as f:
        csv_write = csv.writer(f)
        csv_head = ["股票代码","股票名","涨停次数"]
        csv_write.writerow(csv_head)
    
    for key in sockets_dict:
        print(key)
        number = get_socket_limit_number(key)
        if number >= 2:
            print("股票代码:",key,"股票名:",sockets_dict[key],"涨停次数:",number)
            content = [key,sockets_dict[key],str(number)]
            csv_write.writerow(content)
    f.close()

if __name__ == "__main__":
    all_sockets = get_socket_data()
    get_limit_socket_data(all_sockets)
