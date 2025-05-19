import matplotlib.pyplot as plt
import numpy as np


class Data:
    def __init__(self, dataframe, data_length : int) -> None:
        self.df = dataframe
        arr = np.array(list(range(0, data_length)))

        self.arr = arr
        self.ylength = data_length

    def plot(self, x, Color : str,  Label : str):
        plt.plot(self.arr, x, color=Color, label = Label)
        plt.legend()

    def bar(self, x, y, xColor: str , yColor: str, xLabel : str, yLabel : str):
        plt.bar([0], sum(x), color=xColor, label=xLabel)
        plt.bar([1], sum(y), color=yColor, label=yLabel)
        plt.legend()

    def showplot(self):
        plt.show()
        plt.close("all")

    def cleanvisual(self):
        plt.close("all")
