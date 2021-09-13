#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


import pyexcel as p
import json
import os
import copy
# from pyexcel_xlsx import save_data
# from pyexcel_xlsx import get_data
from collections import OrderedDict
# from pyexcel_xlsx import get_data
# from pyexcel_xlsx import save_data

# def get_inputAge(xlsxPath,sheetname,row_number,colum_name,start_row):
#     """取得输入的年龄值"""
#     # single_Sheet = readexcel(xlsxPath, sheetname)
#     single_Sheet = p.get_sheet(file_name=xlsxPath,sheet_name=sheetname,start_row=start_row,skip_empty_rows=True)
#     ages = readsheet(single_Sheet,row_number, colum_name)
#     ages1 = []
list_plan1 = []
list_plan2 = []
list_plan3 = []
list_plan4 = []
list_plan5 = []
list_plan6 = []
list_plan7 = []
list_plan8 = []

def get_Row(xlsxPath,sheetname,rowname,startrow):
    """取得1行"""
    single_Sheet = p.get_sheet(file_name=xlsxPath, sheet_name=sheetname, start_row=startrow, skip_empty_rows=True)
    single_Sheet.name_rows_by_column(0)
    # for row in single_Sheet.named_rows():
    #     print json.dumps(row,encoding='utf-8',ensure_ascii=False)
    # gole_list = single_Sheet.named_row_at(rowname)
    data_dict = single_Sheet.to_dict()
    return  data_dict[rowname]

def get_dict(xlsxPath,sheetname,startrow):
    """获取整个sheet转化为字典"""
    records = p.get_sheet(file_name=xlsxPath, sheet_name=sheetname, start_row=startrow, skip_empty_rows=True, skip_empty_coloums=True)
    print records
    records.name_rows_by_(0)
    data_dict = records.to_dict()
    print json.dumps(data_dict,encoding='utf-8',ensure_ascii=False)
    return data_dict

def get_list(xlsxPath,sheetname,startrow):
    single_dict = p.get_book_dict(file_name=xlsxPath, sheet_name=sheetname, start_row=startrow, skip_empty_rows=True)
    row_list = single_dict[sheetname]
    # for key,item in single_dict.items():
    # 	print(json.dumps(item, ensure_ascii=False, sort_keys=False, indent=1))
    return row_list



def get_gole_index(p_p,g):

    # print("g=%s" % g)
    if (p_p == '1000' and g == 'M'):
        index = 0
    if p_p == '1000' and g == 'F':
        index = 1
    if p_p == '3' and g =='M':
        index = 2
    if p_p == '3' and g == 'F':
        index = 3
    if p_p == '5' and g == 'M':
        index = 4
    if p_p == '5' and g == 'F':
        index = 5
    if p_p == '10' and g =='M':
        index = 6
    if p_p == '10' and g =='F':
        index = 7
    if p_p == '20' and g =='M':
        index = 8
    if p_p == '20' and g =='F':
        index = 9
    if p_p == '30' and g =='M':
        index = 10
    if p_p == '30' and g =='F':
        index = 11
    # print index
    return  index

def get_free_index(p_p,g):
    print(p_p)
    p_p = str(p_p)
    if (p_p == '2' and g == 'M'):
        index = 0
    if p_p == '2' and g == 'F':
        index = 1
    if p_p == '4' and g =='M':
        index = 2
    if p_p == '4' and g == 'F':
        index = 3
    if p_p == '9' and g == 'M':
        index = 4
    if p_p == '9' and g == 'F':
        index = 5
    if p_p == '19' and g =='M':
        index = 6
    if p_p == '19' and g =='F':
        index = 7
    if p_p == '29' and g =='M':
        index = 8
    if p_p == '29' and g =='F':
        index = 9
    return index

def get_free_fee(fee,amount,xlsxPath,sheetname,start_row,start_column,gender,age,g_p,p_p):
    free_records =  p.get_sheet(file_name=xlsxPath, sheet_name=sheetname, start_row=start_row, start_column=start_column, skip_empty_rows=True,
                          skip_empty_coloums=True)
    # print free_records
    index = get_free_index(p_p=p_p,g=gender)
    # print index
    # print ("age:%d" %age)
    row_index = age
    # print row_index
    value = free_records[row_index,index]
    print value
    fee1 = fee * (amount * 10)
    fee2 = fee1 * 0.001* value
    print(fee1,fee2)
    return  fee1,fee2





def get_mainfee(xlsxPath,sheetname,start_row,start_column,gender,age,g_p,p_p):
    records = p.get_sheet(file_name=xlsxPath, sheet_name=sheetname, start_row=start_row, start_column=start_column, skip_empty_rows=True,
                          skip_empty_coloums=True)
    # print records
    index = get_gole_index(p_p=p_p,g=gender)
    print index
    row_index = age+2
    print row_index
    # print records[6,6]
    value = records[row_index,index]

    return value



#
# if __name__ == '__main__':
#     proDir = r"C:\Users\Administrator\Documents\hexiejiankang"
#     # print os.getcwd()
#     # print os.path.join(os.getcwd())
#     # print proDir
#     xlsxPath = os.path.join(proDir, "data", "main1.xls")
#     records = p.get_sheet(file_name=xlsxPath, sheet_name='30', start_row=5,start_column=1, skip_empty_rows=True, skip_empty_coloums=True)
#     print records
#     records.name_columns_by_row(0)
#     # records.name_rows_by_column(0)
#     data_dict = records.to_dict()
#
#     print json.dumps(data_dict,encoding='utf-8',ensure_ascii=False)
