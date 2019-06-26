import numpy as np
import pandas as pd
import datetime
import argparse
from pathlib import Path


def writer(log_path, save_path):
	df = pd.DataFrame()

	trials = []

	act = []
	act_line = ["Trial ++++++++ active ++++++++"]

	inact = []
	inact_line = ["Trial ------- inactive -------"]

	i = 1
	with open(log_path, 'r') as f:
	    f = f.readlines()

	    for line in f:
	        for phrase in act_line:
	            if phrase in line:
	                onset_str = line[:19]
	                onset_dt = datetime.datetime.strptime(onset_str, '%Y-%m-%d %H:%M:%S')
	                act.append(onset_dt)
	                trials.append(i)
	                i += 1
	                
	        for phrase in inact_line:
	            if phrase in line:
	                offset_str = line[:19]
	                offset_dt = datetime.datetime.strptime(offset_str, '%Y-%m-%d %H:%M:%S')
	                inact.append(offset_dt)
	                
	df['trial'] = trials
	df['timestamp_start_trial'] = act
	df['timestamp_end_trial'] = inact

	writer = pd.ExcelWriter(save_path, engine='xlsxwriter')
	df.to_excel(writer, sheet_name='sheet1')
	writer.save()

if __name__ == '__main__':

	log_path = input('Please enter the path to the log file: ')
	save_path = input('Please enter the directory to which the excel file needs to be saved: ') + '\\timestamps.xlsx'
	writer(log_path=log_path, save_path=save_path)
