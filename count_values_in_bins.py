import numpy as np

def count_values_in_bins(data, bin_edges):
    
    b = bin_edges.size - 1
    counts_per_bin = np.zeros(b)
    
    for i in range(b):
        for value in range(data.size):
            if i == b-1:
                if ((data[value] >= bin_edges[i]) and (data[value] <= bin_edges[i+1])):
                    counts_per_bin[i] += 1
            else:       
                if ((data[value] >= bin_edges[i]) and (data[value] < bin_edges[i+1])):
                    counts_per_bin[i] += 1
    
    return counts_per_bin

data = np.array([-1.0, 0.0, 0.9, 5.0, 6.0])
bin_edges = np.array([0.0, 1.0, 2.0, 5.0])

print(count_values_in_bins(data, bin_edges))

