# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
# def evaluate(line):
#     pd.Timestamp(line[0,20])
#     match_str = re.search(r'\d{4}-\d{2}-\d{2}\ ', line)
#
# pd.DataFrame([evaluate(line) for line in open("D:/Downloads/DataReader/log_example.txt")])
import ast
import re
import numpy as np
import json

txtfile = open("D:/Downloads/DataReader/log_example.txt", "r")
# print(txtfile.readlines()[0])
m=0
t1=0
t2=0
with open('file.json', 'w') as f:


    while (True) :

        line = str(txtfile.readline())

        if not line:
            break

        splitted_array = re.split("\s{2,}", line)
        # print(splitted_array)
        # print(splitted_array)
        splitted_array[0] = pd.Series(splitted_array[0])
        splitted_array[0] = pd.to_datetime(splitted_array[0])
        if (splitted_array[2] =="Main"):
            m=m+1
        else:
            if(splitted_array[2] =="T1_measure"):
                t1=t1+1
            else:
                t2=t2+1
        Logs=["DATETIME","MSG_TYPE","MODULE_NAME","MESSAGE"]
        Logs_dictionary = dict(zip(Logs, splitted_array))
        # print(Logs_dictionary)

print(m,t1,t2)

