from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import pandas as pd
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
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

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
