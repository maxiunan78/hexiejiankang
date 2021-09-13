#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os
from decimal import *
inputlist = []

option_responsibility1 = ['0','1']
option_responsibility2 = ['0','1']
option_responsibility3 = ['0','1']

inputlist = []



def get_totalfee(resp,amount,mainfee,optional1fee):


		if (resp == []):
			respect_fee = mainfee
			# print mainfee
			print(resp)
			respect_fee = Decimal(str(respect_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp,respect_fee


		if (resp == "B10018"):
			respect_fee = mainfee + optional1fee*mainfee*0.001
			print(resp)
			print(mainfee)
			print (optional1fee*mainfee*0.001)
			print("111111111当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			respect_fee = Decimal(str(respect_fee)).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
			return resp,respect_fee


		if (resp == ["B10016"]):
			# respect_fee = mainfee + optional2fee
			# print(resp)
			# respect_fee = Decimal(str(respect_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
			# # print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			# return resp,respect_fee
			pass


		if (resp == ["B10017"]):
			# respect_fee = mainfee + optional3fee
			# print(resp)
			# respect_fee = Decimal(str(respect_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
			# # print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			# return resp,respect_fee
			pass



		if (resp == ["B10018", "B10016"]):
			# respect_fee = mainfee + optional2fee + optional1fee*(mainfee + optional2fee)*0.001
			# print(resp)
			# # print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			# respect_fee = Decimal(str(respect_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
			# return resp, respect_fee
			pass


		if (resp == ["B10018", "B10017"]):
			# respect_fee = mainfee + optional1fee*(mainfee + optional3fee)*0.001 +  optional3fee
			# print(resp)
			# respect_fee = Decimal(str(respect_fee)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
			# # print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			# return resp, respect_fee
			pass


		if (resp == ["B10016", "B10017"]):
			respect_fee = mainfee + optional2fee +  optional3fee
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp,round(respect_fee,2)



		if (resp == ["B10018", "B10016", "B10017"]):
			respect_fee = mainfee + optional2fee +  optional3fee + optional1fee*(mainfee + optional2fee + optional3fee)*0.001
			print(resp)
			# print("当前保额:%f,当前总保费:%f" % (amount, respect_fee))
			return resp,round(respect_fee,2)


# if __name__ == '__main__':
# 	getResponsibility()