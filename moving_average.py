import numpy as np

def moving_average(signal, window_size):
    k = (window_size - 1) // 2
    smooth_arr = np.zeros(signal.size, dtype = float)
    
    n = len(signal)
    
    for i in range(n):
        
        avg = 0
        num = 0
        
        for j in range(max(0, i - k), min(n - 1, i + k) + 1):
            avg += signal[j]
            num += 1
        
        avg /= num
        
        smooth_arr[i] = avg
    
    return smooth_arr
