# CS120: Capitol Technology University. Prof. Mehri
# Assignment 04 Solution

import exceptions
import numpy as np
import matplotlib.pyplot as plt


def openFile(fileName, data):
    try:
        with open(fileName, "r") as f:
            for line in f:
                currentData = line[:-2]
                data.append(currentData)
    except exceptions.IOError:
        print("File not found")
        return False
    else:
        f.close()
        return True

def makeChoice():
    choice = 0
    while choice < 1 or choice > 2:
        print("Pick a Plot Style\n"
              "1. Line Graph\n"
              "2. Bar Graph")
        try:
            choice = int(input("Enter your numerical choice: "))
        except:
            print("Enter a numerical value only")
    return choice


def plotLine(data):
    yPoints = np.array(data)
    plt.plot(yPoints)
    plt.xlabel("Weeks of 1994")
    plt.ylabel("Weekly Average")
    plt.show()


def plotBar(data):
    height = []
    for item in data:
        height.append(float(item))

    avg = []
    for count in range(1, 53):
        avg.append('W' + str(count))
    bars = tuple(avg)
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.show()

def main():
    myData = []
    fileName = "1994_Weekly_Gas_Averages.txt"
    if openFile(fileName, myData):
        print("File found")
        # print(myData)
        choice = makeChoice()
        if choice == 1:
            plotLine(myData)
        else:
            plotBar(myData)
main()








