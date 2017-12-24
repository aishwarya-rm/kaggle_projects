import csv, os, sys

def load_csv(filename):
	lines = []
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		for line in reader:
			lines.append(line)

	return lines

def extract_features(raw):
	val_names = raw.pop(0)[1:]
	data_set = []
	id = 1
	for row in raw:
		data_point = {}
		vals = []
		data_point['id'] = id
		for r in row[1:]:
			vals.append(float(r))
		data_point['vals'] = vals
		data_set.append(data_point)
	return val_names, data_set

def load_data():
	lines = load_csv("train.csv")
	return extract_features(lines)
