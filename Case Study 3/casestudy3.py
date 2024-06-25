import statistics  # import the statistics library

# Data: infection rates
infection_rates = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412,
                   1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

# Calculate statistics
minimum = min(infection_rates)  # Calculate the minimum value in the list
maximum = max(infection_rates)  # Calculate the maximum value in the list
# Calculate the range (difference between maximum and minimum)
range_value = maximum - minimum
# Calculate the mean (average) of the data
mean_value = statistics.mean(infection_rates)
# Calculate the median (middle value) of the data
median_value = statistics.median(infection_rates)
# Calculate the variance of the data
variance_value = statistics.variance(infection_rates)
# Calculate the standard deviation of the data
std_deviation = statistics.stdev(infection_rates)

# Display the statistics
print(f"Minimum: {minimum}")  # Print the minimum value
print(f"Maximum: {maximum}")  # Print the maximum value
print(f"Range: {range_value}")  # Print the range value
print(f"Mean: {mean_value}")  # Print the mean value
print(f"Median: {median_value}")  # Print the median value
print(f"Variance: {variance_value}")  # Print the variance value
# Print the standard deviation value
print(f"Standard Deviation: {std_deviation}")
