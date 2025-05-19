from pandas import read_csv
from lib.visual import Data
import numpy

df = read_csv("./enrolees.csv", index_col=0)

x = df["1st Year Male"]
female = df["1st Year Female"]

x = numpy.array(x)

print(x)

lengthh = len(x)

data = Data(df, lengthh)


data.plot(x=x, Color="pink", Label="1ST YEAR male")
data.plot(x=female, Color="blue", Label="1st year female")
#data.bar(x=female, y=x , Color="blue", Label="1st Year female")
data.bar(x, y=female, xColor="pink", yColor="blue", xLabel="1st Year male", yLabel="1st Year Female")

data.showplot()

print(df)
