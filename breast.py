import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

"""
Load Data from CSV file
"""


input_file = 'wdbc.data.csv'
df = pd.read_csv(input_file, header = 0)
original_headers = list(df.columns.values)
df = df._get_numeric_data()
numeric_headers = list(df.columns.values)


def loadData():
	rawData = pd.read_csv(filepath_or_buffer='wdbc.data.csv', header = 0)
	return rawData

def processData(data):
	original_headers = list(data.columns.values)
	data = data._get_numeric_data()
	numeric_headers = list(data.columns.values)

	return

def main():
	print(df.values)


if __name__ == "__main__":
	main()
