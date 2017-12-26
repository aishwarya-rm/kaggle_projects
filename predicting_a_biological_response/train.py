from kmean import choose_centers, train_kmean, sum_of_within_group_ss
from data import load_data
import os, sys

val_names, data_set = load_data()
iter_limit = 10

init_centers = choose_centers(data_set, 2)
centers, clusters, num_iterations = train_kmean(data_set, init_centers, iter_limit)
print str(sum_of_within_group_ss(clusters, centers))
