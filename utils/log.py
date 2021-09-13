#!/usr/bin/env python
#-*- coding:utf-8 -*-
import datetime
import os
import logging

class log:

    def __init__(self):

        global logPath, resultPath, proDir1
        proDir1 = os.path.split(os.getcwd())[0]
        resultPath = os.path.join(proDir1, "log")
        # create result file if it doesn't exist
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        logPath = os.path.join(resultPath, str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler(os.path.join(logPath, "mylog.log"))
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

# if __name__ == '__main__':
#     log().logger.info("lellele")
