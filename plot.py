import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'Installed Capacity.csv'  # Adjust the file path
data = pd.read_csv(file_path)
data['Date Time Hour Beginning'] = pd.to_datetime(data['Date Time Hour Beginning'], format='%Y/%m/%d %H:%M')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(data['Date Time Hour Beginning'], data['Installed Eskom Capacity'], label='Installed Capacity', color='blue')
plt.xlabel('Date Time')
plt.ylabel('Installed Eskom Capacity')
plt.title('Installed Eskom Capacity Over Time')
plt.grid(True)
plt.legend()

# Save the plot as an image file
plt.savefig('static_plot.png')
