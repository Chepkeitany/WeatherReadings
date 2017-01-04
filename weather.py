# Open file in read mode
# Read files from the third line to the second-last element
with open('weather.dat', 'r') as f:
    weather_records = f.readlines()[2:-1]

# Initialize an empty array to store contents of the file for easy processing
daily_weather_records = []

# Add each line of the weather record to the array
# while split the line using spaces
for line in weather_records:
    daily_weather_records += [line.split()]


# Function to get the day of the month with maximumspread
def maximumspread(daily_weather_records):
    # initialize a variable to keep track of maximum difference
    # between MxT and MnT
    max = 0
    for x in daily_weather_records:
        spread = int(x[1].replace('*', '')) - int(x[2].replace('*', ''))
        if spread > max:
            max = spread
            day = x[0]
    print day, max


maximumspread(daily_weather_records)
