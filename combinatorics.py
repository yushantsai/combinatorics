import sys
import argparse
import numpy as np

def main():
    method = "C"
    numberOfSet = 3
    numberOfSubSet = 1
    result = 0

    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--method", type = str, default = method, help = "The applied method")
    parser.add_argument("-ns", "--set", type = int, default = numberOfSet, help = "The number of set")
    parser.add_argument("-nss", "--subset", type = int, default = numberOfSubSet, help = "The number of subset")

    args = parser.parse_args()

    method = args.method.upper()
    numberOfSet = args.set
    numberOfSubSet = args.subset

    if method == "C":
        result = getCResult(numberOfSet, numberOfSubSet)
        result = getPResult(numberOfSet, numberOfSubSet)
    elif method == "H":
        result = getHResult(numberOfSet, numberOfSubSet)
    elif method == "U":
        result = getUResult(numberOfSet, numberOfSubSet)
    else:
        result = None

    if result == None:
        print "Oops! this method is not included."
    else:
        print getMathodAlias(method) + ": "
        print "\t" + str(numberOfSet) + method + str(numberOfSubSet) + " = " + str(result)

def getMathodAlias(method):
    if method == "C":
        return "Combination"
    elif method == "P":
        return "Permutation"
    elif method =="H":
        return "Repeated Combination"
    elif method == "U":
        return "Repeated Permutation"
    else:
        return None

def getCResult(numberOfSet, numberOfSubSet):
    return factorial(numberOfSet) / (factorial(numberOfSubSet) * factorial(numberOfSet - numberOfSubSet))

def getPResult(numberOfSet, numberOfSubSet):
    return factorial(numberOfSet) / factorial(numberOfSet - numberOfSubSet)

def getHResult(numberOfSet, numberOfSubSet):
    return factorial(numberOfSet + numberOfSubSet - 1) / (factorial(numberOfSubSet) * factorial(numberOfSet - 1))

def getUResult(numberOfSet, numberOfSubSet):
    return pow(numberOfSet, numberOfSubSet)

def factorial(num):
    if num == 0:
        return 1
    else:
        return np.prod(range(1, num + 1))

def isInt(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
