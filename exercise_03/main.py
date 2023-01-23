import numpy as np
sampl = np.random.uniform(low=0, high=1, size=(10))
print("Random Numbers: ")
print(sampl)
print("Mean: ", np.mean(sampl), " Median: " , np.median(sampl), " Standard Deviation: " , np.std(sampl))