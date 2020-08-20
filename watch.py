#!/usr/bin/python
#coding=utf8
"""
# Author: zhangyi
# Created Time : 2020-04-07 23:11:59

# File Name: main.py
# Description:

"""
import tushare
import pandas
import time
import io
import sys

if __name__ == "__main__":
    while True:
        code=["600895"]
        dataNow=tushare.get_realtime_quotes(code)
        # print(dataNow) 
        for i in range(len(code)) :
            name = dataNow['name'].values[i]
            stock_code = code[i]
            price = dataNow['price'].values[i]
            pre_close = dataNow['pre_close'].values[i]
            rate = ( float(price) - float(pre_close)) / float(pre_close) *100 
            print(name,"code:",stock_code,"现价:",price,"涨跌幅:","%.2f" %rate,"%")
            
        time.sleep(2)
        print("\n")


