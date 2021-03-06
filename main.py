import pandas as pd
import plotly_express as px
import re
import numpy as np
import json
import time
from flask import Flask
import matplotlib

from flask import json
app = Flask(__name__)
txtfile = open("D:/Downloads/DataReader/log_example.txt", "r")

@app.route('/logs')
def logs():
    start = time.time()
    m,t1,t2,mainErrors,t1Errors,t2Errors = 0,0,0
    first_line = str(txtfile.readline())
    first_date=first_line[0:10]
    newArray=[]
    while (True):
            line = str(txtfile.readline())
            if not line:
                break
            #splitting data having more 2 spaces or more
            splitted_array = re.split("\s{2,}", line)
            if splitted_array!=None:
                newArray.append(splitted_array)
            if (splitted_array[2] == "Main"):
                m = m + 1
            else:
                if (splitted_array[2] == "T1_measure"):
                    t1 = t1 + 1
                else:
                    t2 = t2 + 1
    #converting to numpy in order to be able to convert to dataframe
    msgType = np.array(newArray)[:, 1]
    module = np.array(newArray)[:, 2]
    message = np.array(newArray)[:, 3]
    threeColumns = np.array([msgType, module])
    df = pd.DataFrame(data=threeColumns)
    # swap rows and columns
    df = pd.DataFrame.transpose(df)
    print(df)
    # counting how much each module name has the same message type
    count = pd.crosstab(df[0], df[1])
    print(count)

    nested_dictionary = {
        "date": first_date,
        "operations": {
            "Main": m,
            "T1_Measure": t1,
            "T2_Measure": t2
        },
        "errors": {
            "Main": int(count.values[0][0]),
            "T1_Measure": int(count.values[0][1]),
            "T2_Measure": int(count.values[0][2]),

        },
        "errors_percentage": {
            "Main": count.values[0][0] / m,
            "T1_Measure": count.values[0][1] / t1,
            "T2_Measure": count.values[0][2] / t2

        },
    }
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    #converting dictionary to json type
    return json.dumps(nested_dictionary)
#histogram to show different message type that visualize low number of error message types
@app.route('/histogram')
def hist():
    txtfile = open("D:/Downloads/DataReader/log_example.txt", "r")
    newArray=[]
    while (True):

            line = str(txtfile.readline())

            if not line:
                break

            splitted_array = re.split("\s{2,}", line)

            if splitted_array!=None:
                newArray.append(splitted_array)

    # using numpy array to take columns instead of rows
    msgType=np.array(newArray)[:, 1]
    module=np.array(newArray)[:, 2]
    message=np.array(newArray)[:, 3]
    threeColumns=np.array([msgType,module,message])

    df = pd.DataFrame(data=threeColumns)
    # swap rows and columns
    df=pd.DataFrame.transpose(df)
    print(df)

    fig = px.histogram(df, x=df[0], color=df[0], color_discrete_sequence=["#871fff", "#ffa78c","#0fa07c"])
    fig.show()


if __name__ == "__main__":
    app.run(host='localhost', port=5000)




