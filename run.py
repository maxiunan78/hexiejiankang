#!/usr/bin/env python
#-*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import os
import utils.send as send
import unittest
import  utils.responsibility as res
import pyexcel as py
from utils.log import log
import json
import pdb
import copy
# from utils import send
import logging
import datetime
import time

import utils.excelUtil as ex
from decimal import *
# import utils.plan

proDir = r'C:\Users\Administrator\Documents\hexiejiankang'
# print os.getcwd()
# print os.path.join(os.getcwd())
# print proDir
xlsxPath = os.path.join(proDir, "data", u"投保人豁免1.xls")
xlsxPath1 = os.path.join(proDir, "data", "main1.xls")
xlsxPath2 = os.path.join(proDir, "data", "main1_and_optional.xls")
xlsxPath3 = os.path.join(proDir, "data", "main2.xls")
xlsxPath4 = os.path.join(proDir, "data", "main2_and_optional.xls")
# print(xlsxPath)

# global error_data
# mydata = json.loads(error_data)

class TestUnderwriting(unittest.TestCase):
    """测试趸交"""

    def setUp(self):
        global logPath, resultPath, proDir1
        proDir1 = os.getcwd()
        resultPath = os.path.join(proDir1, "log")
        # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler(os.path.join(logPath, "my.log"))
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.log = log()
        # print type(self.log)
        self.num = 0
        self.gender = ['M', 'F']
        self.guarantee_periods = ['30','70','80']
        # 保30年缴费期限
        self.Payment_period1 = ['1000','3','5','10','20']
        # 保至70 ，保至80
        self.Payment_period2 = ['1000','3','5','10','20','30']
        self.way = ['913200','913201']
        # self.nowamount = 100000
        self.insured_amount1 = [10,20,30]
        # 被保人年龄∈(0 - 9]时，最高30万
        self.insured_amount2 = [10,20,30,40,50]
        # 被保人年龄∈(10 - 17]时，最高50万
        #
        # 方式一：913200
        # 方式二：913201
        self.secondDiseases = ['0','1']
        self.holderImmunity=['0','1']
        # 投保人年龄
        self.age2 = range(18,51,1)
        # 被保人年龄
        self.age1 = range(0,18,1)
        self.log.logger.info('test start1')

    def test_a(self):
        """测试"""
        # mydata[]
        for g in self.gender:
            self.log.logger.info("性别:%s" %g)
            print("性别:%s" %g)
            for a in self.age1:
                self.log.logger.info ("年龄：%d" %a )
                print ("年龄：%d" %a )
                # self.log.logger.info ("*****************************************************")
                print("*****************************************************")
                for gu_period in self.guarantee_periods:
                    print("********* 保障期限：%s **********" %gu_period)
                    self.log.logger.info("********* 保障期限：%s **********" %gu_period)
                    if(gu_period=='30'):
                        gole_payment = self.Payment_period1
                    else:
                        gole_payment = self.Payment_period2
                    for go in gole_payment:
                        print ("*****************")
                        print ("缴费期限：%s" %go)
                        self.log.logger.info("**************缴费期限：%s"%go)
                        # print ('\n')
                        for w in self.way:
                            for i in self.secondDiseases:
                                for h in self.holderImmunity:
                                    if(a<=9):
                                        gole_insured_amount = self.insured_amount1
                                    else:
                                        gole_insured_amount = self.insured_amount2

                                    for amount in gole_insured_amount:
                                        #保额循环

                                        if(w=='913200' and i =='0'):
                                            print"方式一，必选保费"
                                            self.log.logger.info("方式一，必选保费")
                                            respect_main1fee = ex.get_mainfee(xlsxPath=xlsxPath1,sheetname=gu_period,start_row=3,start_column=1,gender=g,age=a,g_p=gu_period,p_p=go)
                                            if(h=='0'):
                                                totalfee = Decimal(str(respect_main1fee*(amount*10))).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
                                            if (h == '1'):

                                                if(go=='1000'):
                                                    print"不能选择投保人豁免，没有豁免费用"

                                                    continue
                                                else:
                                                    fee1,free_fee  = ex.get_free_fee(fee=respect_main1fee,amount=amount,xlsxPath=xlsxPath,sheetname='holder_exemption',start_row=5,start_column=1,gender=g,age=a,g_p=gu_period,p_p=int(go)-1)
                                                    print("投保人豁免费用：%f" % free_fee)
                                                    totalfee = Decimal(str(fee1)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP) + Decimal(str(free_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

                                        if(w=='913200' and i =='1'):
                                                print"方式一，必选保费+二次重大疾病"
                                                self.log.logger.info("方式一，必选保费+二次重大疾病")
                                                respect_main1_and_optional_fee = ex.get_mainfee(xlsxPath=xlsxPath2, sheetname=gu_period,
                                                                                  start_row=3, start_column=1, gender=g, age=a,
                                                                                  g_p=gu_period, p_p=go)
                                                if (h == '0'):
                                                    totalfee = Decimal(str(respect_main1_and_optional_fee * (amount * 10))).quantize(
                                                        Decimal('0.00'), rounding=ROUND_HALF_UP)
                                                if (h == '1'):

                                                    if(go=='1000'):
                                                        print"不能选择投保人豁免，没有豁免费用"
                                                        continue
                                                    else:
                                                        fee1,free_fee  = ex.get_free_fee(fee=respect_main1_and_optional_fee,amount=amount,xlsxPath=xlsxPath,sheetname='holder_exemption',start_row=5,start_column=1,gender=g,age=a,g_p=gu_period,p_p=int(go)-1)
                                                        print fee1,free_fee
                                                        totalfee = Decimal(str(fee1)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP) + Decimal(str(free_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

                                        if(w=='913201' and i =='0'):
                                            print"方式二，必选保费"
                                            self.log.logger.info("方式二，必选保费")
                                            respect_main2fee = ex.get_mainfee(xlsxPath=xlsxPath3, sheetname=gu_period, start_row=3,
                                                                               start_column=1, gender=g, age=a, g_p=gu_period,
                                                                               p_p=go)
                                            if (h == '0'):
                                                totalfee = Decimal(
                                                    str(respect_main2fee * (amount * 10))).quantize(
                                                    Decimal('0.00'), rounding=ROUND_HALF_UP)
                                            if (h == '1'):

                                                if (go == '1000'):
                                                    print"不能选择投保人豁免，没有豁免费用"
                                                    continue
                                                else:
                                                    fee1, free_fee = ex.get_free_fee(fee=respect_main2fee,
                                                                                         amount=amount, xlsxPath=xlsxPath,
                                                                                         sheetname='holder_exemption',
                                                                                         start_row=5, start_column=1,
                                                                                         gender=g, age=a, g_p=gu_period,
                                                                                         p_p=int(go) - 1)

                                                    totalfee = Decimal(str(fee1)).quantize(Decimal('0.00'),
                                                                                           rounding=ROUND_HALF_UP) + Decimal(
                                                        str(free_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

                                        if(w=='913201' and i =='1'):
                                            print"方式二，必选保费+二次重大疾病"
                                            respect_main2_and_optional_fee = ex.get_mainfee(xlsxPath=xlsxPath4, sheetname=gu_period, start_row=3,
                                                                                start_column=1, gender=g, age=a, g_p=gu_period,
                                                                                    p_p=go)
                                            if (h == '0'):
                                                totalfee = Decimal(
                                                    str(respect_main2_and_optional_fee * (amount * 10))).quantize(
                                                    Decimal('0.00'), rounding=ROUND_HALF_UP)
                                            if (h == '1'):

                                                if (go == '1000'):
                                                    print"不能选择投保人豁免，没有豁免费用"
                                                    continue
                                                else:
                                                    fee1, free_fee = ex.get_free_fee(fee=respect_main2_and_optional_fee,
                                                                                         amount=amount, xlsxPath=xlsxPath,
                                                                                         sheetname='holder_exemption',
                                                                                         start_row=5, start_column=1,
                                                                                         gender=g, age=a, g_p=gu_period,
                                                                                         p_p=int(go) - 1)

                                                    totalfee = Decimal(str(fee1)).quantize(Decimal('0.00'),
                                                                                           rounding=ROUND_HALF_UP) + Decimal(
                                                        str(free_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

                                #

                                        data = [

                                            # "productId": "100007",  # 产品编码
                                            # "planId": "100010",  # 计划编码json_senddata
                                            {"code":"age","value":str(a)},# 被保人年龄
                                            {"code": "gender", "value": g},  # 被保人性别
                                            {"code": "guaranteePeriod", "value": gu_period},  # 保障期限
                                            {"code": "paymentPeriod", "value":go},  # 交费期限
                                            {"code": "diePayMethod", "value":w},  # 身故给付方式
                                            {"code": "secondDiseases", "value":i },  # 第二次重大疾病保险金
                                            {"code": "guaranteeAmount", "value":str(amount)},  # 保障金额
                                            {"code": "holderImmunity", "value": h},  # 投保人豁免
                                            {"code": "holderGender", "value":g},  # 豁免投保人性别
                                            {"code": "holderAge", "value": str(a+18)},
                                        ]
                                        json_senddata = json.dumps(data,encoding='utf-8',ensure_ascii=False,indent=2,separators=(',', ': '))
                                        print(json_senddata)
                                        self.log.logger.info('\n'+json_senddata)
                                        retext = send.senddatas(data)

                                        # print (retext.text)
                                        # print (a)
                                        # outputdata = retext.text["data"]["price"]
                                        outputdata = json.loads(retext.text)["data"]["price"]
                                        outputdata =  Decimal(str(outputdata)).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
                                        times = str(datetime.datetime.now().hour) + ":" + str(
                                            datetime.datetime.now().minute) + ":" + str(
                                            datetime.datetime.now().second)
                                        retval = os.getcwd()
                                        fileDay = time.strftime("%Y%m%d", time.localtime())
                                        recordpath = os.path.join(retval,"reords")
                                        if not os.path.exists(recordpath):
                                            os.mkdir(recordpath)

                                        file = open( recordpath+'\\'+fileDay+'.txt', 'a+')
                                        file.write("\n\n----------%s----------"
                                                   "\n被保人年龄：%d \n"
                                                   "保障期限：%s\n"
                                                   "交费期限:%s\n"
                                                   "身故给付方式:%s\n"
                                                   "第二次重大疾病保险金:%s\n"
                                                   "保障金额:%d\n"
                                                   "投保人豁免：%s"
                                                   "接口返回结果：%f   计算结果：%f\n" % ("测试结果记录",a, gu_period, go, w, i,amount,h, outputdata, totalfee))
                                        file.close()
                                        if (totalfee != outputdata):
                                            print (totalfee, outputdata)
                                        # with self.subTest():
                                        # number = len(str(float(totalfee)).split('.')[1])
                                        # if number == 1:
                                        #     finalfee = str(float(totalfee)) + "0"
                                        # else:
                                        #     finalfee = str(float(totalfee))
                                        try:
                                            self.assertEqual(totalfee, outputdata, msg="结果不匹配！")
                                        except AssertionError as e:
                                            print("该条用例未通过")
                                            self.log.logger.info("该条用例未通过")
                                            self.log.logger.info("发送数据：")
                                            self.log.logger.info(json_senddata)
                                            error_data = json_senddata
                                            self.log.logger.info(str(totalfee),str(outputdata))
                                            raise e
                                        else:
                                            print("该条用例通过")






    def tearDown(self):
        print("test  end")

if __name__ == '__main__':
    unittest.main()
