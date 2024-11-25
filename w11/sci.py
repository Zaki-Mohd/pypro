from scipy import stats

# Finding mean and mode of a dataset
data = [1, 2, 2, 3, 4]
mean = stats.tmean(data)
mode = stats.mode(data)
print(f"Mean: {mean}, Mode: {mode[0]}")
