import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/pranalikulkarni/Documents/Career/Updated Resume 05:22/Prep/Uber project/uber_dataset.csv')
# Strip any leading/trailing spaces in column names
df.columns = df.columns.str.strip()

print(df)
# 1. Which date had the most completed trips during the two week period?
# Group by Date and sum Completed Trips
trips_per_date = df.groupby('Date')['Completed Trips'].sum()
# Find the date with the most completed trips
most_trips_date = trips_per_date.idxmax()
most_trips_count = trips_per_date.max()

print(f"1) The date with the most completed trips is {most_trips_date} with {most_trips_count} trips.")
#----------------------------------------
# 2. What was the highest number of completed trips within a 24 hour period?
print(f"2) The highest number of completed trips within a 24 hour period is {most_trips_count} on {most_trips_date}")
#----------------------------------------
# 3. Which hour of the day had the most requests during the two week period?
#Group by Time(hour) and sum the Requests
trips_perhour = df.groupby('Time (Local)')['Requests'].sum()
most_trips_hour = trips_perhour.idxmax()

print(f"3) {most_trips_hour}th hour had the most requests during the two week period")
#----------------------------------------

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time (Local)'].astype(str) + ':00', format='%d-%b-%y %H:%M')
zero_trips = df[df['Completed Trips']== 0].copy()

zero_trips['weekday'] = zero_trips['DateTime'].dt.weekday
zero_trips['hour'] = zero_trips['DateTime'].dt.hour

def is_weekend(row):
    if row['weekday'] == 4 and row['hour'] >= 17:  # Friday after 5 PM
        return True
    if row['weekday'] == 5:  # Saturday
        return True
    if row['weekday'] == 6 and row['hour'] < 3:  # Sunday before 3 AM
        return True
    return False

zero_trips['is_weekend'] = zero_trips.apply(is_weekend, axis=1)

weekend_zeroes = zero_trips['is_weekend'].sum()
total_zeroes = len(zero_trips)
percentage = (weekend_zeroes / total_zeroes) * 100 if total_zeroes > 0 else 0

print(f"4) Percentage of all zeroes during the two week period that occurred on weekend: {percentage:.2f}%")
#----------------------------------------
# 4. What is the weighted average ratio of completed trips per driver during the two week period? Tip: "Weighted average" means your answer should account for the total trip volume in each hour to determine the most accurate number in whole period.

# Group by hour of day and sum requests across all days
requests_per_hour = df.groupby(df['Time (Local)'])['Requests'].sum().sort_index()

# Convert to numpy array for rolling sum
requests_array = requests_per_hour.values

# Calculate rolling sum for 8-hour windows
window_size = 8
rolling_sums = np.convolve(requests_array, np.ones(window_size, dtype=int), 'valid')

# Find the start hour of the busiest window
busiest_start_hour = rolling_sums.argmax()
busiest_end_hour = busiest_start_hour + window_size - 1
busiest_total_requests = rolling_sums.max()

print(f"6) The busiest 8 consecutive hours are from {busiest_start_hour}:00 to {busiest_end_hour}:59 with {busiest_total_requests} unique requests over the two week period.")

# # 7. Driver supply always increases when demand increases during the two week period.
# print ('7) FALSE. Driver Suppy does not always increase proportionally when demand increases, during the two week period') 

plt.figure(figsize=(15,6))
plt.plot(df['DateTime'], df['Requests'], label='Requests (Demand)')
plt.plot(df['DateTime'], df['Unique Drivers'], label='Drivers (Supply)')
plt.xlabel('DateTime')
plt.ylabel('Count')
plt.legend()
plt.title('Demand vs Driver Supply Over Time')
# plt.show()
print("7) FALSE")

# 8. In which 72 hour period is the ratio of Zeroes to Eyeballs the highest?
# Create a column for Zeroes (1 if Completed Trips == 0, else 0)
df['Zeroes'] = (df['Completed Trips'] == 0).astype(int)

# Sort by DateTime to ensure correct rolling window
df = df.sort_values('DateTime').reset_index(drop=True)

# Calculate rolling sums for 72-hour window
window_size = 72
df['Zeroes_rolling'] = df['Zeroes'].rolling(window=window_size).sum()
df['Eyeballs_rolling'] = df['Eyeballs'].rolling(window=window_size).sum()

# Avoid division by zero
df['Zeroes_to_Eyeballs'] = df['Zeroes_rolling'] / df['Eyeballs_rolling'].replace(0, np.nan)

# Find the 72 hour window with the highest ratio
max_idx = df['Zeroes_to_Eyeballs'].idxmax()
max_start_time = df.loc[max_idx - window_size + 1, 'DateTime']
max_end_time = df.loc[max_idx, 'DateTime']
max_ratio = df.loc[max_idx, 'Zeroes_to_Eyeballs']

print(f"8) The 72-hour period with the highest ratio of Zeroes to Eyeballs is from {max_start_time} to {max_end_time}, with a ratio of {max_ratio:.4f}.")

# Group by hour of day and calculate total Zeroes and Eyeballs
hourly = df.groupby(df['DateTime'].dt.hour).agg({'Zeroes': 'sum', 'Eyeballs': 'sum'})

# Calculate Zeroes to Eyeballs ratio for each hour
hourly['Zeroes_to_Eyeballs'] = hourly['Zeroes'] / hourly['Eyeballs'].replace(0, np.nan)

# Find the hour with the highest ratio
best_hour = hourly['Zeroes_to_Eyeballs'].idxmax()
best_ratio = hourly['Zeroes_to_Eyeballs'].max()

print(f"9) 5 drivers can be added to hour {best_hour}:00 each day, which has the highest average Zeroes to Eyeballs ratio ({best_ratio:.4f}) over the two week period.")

print("10) TRUE")

hourly_means = df.groupby(df['DateTime'].dt.hour).agg({
    'Requests': 'mean',
    'Unique Drivers': 'mean'
})

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(hourly_means.index, hourly_means['Requests'], label='Avg Requests')
plt.plot(hourly_means.index, hourly_means['Unique Drivers'], label='Avg Unique Drivers')
plt.xlabel('Hour of Day')
plt.ylabel('Average Count')
plt.title('Average Demand and Supply by Hour of Day')
plt.legend()
# 
print("11) 4:00 AM often makes the most sense as a ""true end day"" for operational or reporting purposes, rather than midnight.")


