# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...

# Filter schools with the best math results (at least 80% of 800)
best_math_schools = schools[schools['average_math'] >= 0.8 * 800][['school_name', 'average_math']]
best_math_schools = best_math_schools.sort_values(by='average_math', ascending=False)

# Calculate total SAT score
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# Get the top 10 performing schools based on total SAT score
top_10_schools = schools[['school_name', 'total_SAT']].sort_values(by='total_SAT', ascending=False).head(10)

# Calculate standard deviation of total SAT score by borough
borough_stats = schools.groupby('borough')['total_SAT'].agg(['mean', 'std', 'count']).reset_index()
borough_stats.columns = ['borough', 'average_SAT', 'std_SAT', 'num_schools']

# Find the borough with the largest standard deviation in total SAT score
largest_std_dev = borough_stats.sort_values(by='std_SAT', ascending=False).head(1)
largest_std_dev = largest_std_dev.round(2)
