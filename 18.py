import pandas as pd
data = {
    'City': ['CityA', 'CityA', 'CityA', 'CityB', 'CityB', 'CityB', 'CityC', 'CityC', 'CityC'],
    'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-02', '2022-01-03'],
    'Temperature': [20, 22, 18, 25, 23, 26, 30, 28, 32]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
mean_temperatures = df.groupby('City')['Temperature'].mean()
std_dev_temperatures = df.groupby('City')['Temperature'].std()
temperature_range = df.groupby('City')['Temperature'].max() - df.groupby('City')['Temperature'].min()
city_with_highest_range = temperature_range.idxmax()
most_consistent_city = std_dev_temperatures.idxmin()
print("Mean Temperatures:")
print(mean_temperatures)
print("\nStandard Deviations of Temperatures:")
print(std_dev_temperatures)
print(f"\nCity with the Highest Temperature Range: {city_with_highest_range}")
print(f"City with the Most Consistent Temperature: {most_consistent_city}")
