import os, sys, random

def choose_centers(data_set, k):
	centers = []
	samples = random.sample(data_set, k)
	for s in samples:
		centers.append(list(s['vals']))
	return centers

def dist(vals, center):
	d = 0.0
	for i in range(len(vals)):
		d += pow(vals[i] - center[i], 2)
	return pow(d, .5)

def get_nearest_center(vals, centers):
	c_idx = 0
	distance = sys.maxint
	for i in range(len(centers)):
		curr = dist(vals, centers[i])
		if curr < distance:
			c_idx = i 
			distance = curr

	return c_idx

def vect_add(x, y):
	s = []
	for i in range(len(x)):
		s.append(x[i] + y[i])
	return s
def vect_avg(s, n):
	avg = []
	for i in range(len(s)):
		avg.append(float(s[i]/n))
	return avg

def recalculate_centers(clusters):
	centers = []
	for c in clusters:
		s = []
		for pt in c:
			if not s:
				s = pt['vals']
			else:
				s = vect_add(s, pt['vals'])
		mean = vect_avs(s, len(c))
		centers.append(mean)
	return centers

def train_kmean(data_set, centers, iter_limit):
	clusters = [[] for x in range(len(centers))]
	num_iterations = 0
	while num_iterations < iter_limit:
		old = clusters
		cluseters = [[] for x in range(len(centers))]
		for point in data_set:
			idx = get_nearest_center(point['vals'], centers)
			clusters[idx].append(point)
		centers = recalculate_centers(clusters)
		num_iterations += 1
		if clusters == old:
			break
	return centers, clusters, num_iterations