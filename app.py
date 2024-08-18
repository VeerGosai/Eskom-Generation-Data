import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

def create_plot(data):
    # Debugging output to ensure data is as expected
    print("DataFrame Columns:", data.columns)
    print("DataFrame Head:\n", data.head())
    
    # Create the plot
    sns.set(style="whitegrid")
    sns.barplot(x="Category", y="Value", data=data)
    
    # Save the plot to a bytes buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    
    # Convert the buffer to a base64-encoded string
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    if request.files and 'file' in request.files:
        csv_file = request.files['file']
        data = pd.read_csv(csv_file)
    elif request.form.get('data_list'):
        data_list = eval(request.form.get('data_list'))
        data = pd.DataFrame(data_list, columns=["Category", "Value"])
    else:
        return "No data provided", 400
    
    plot_url = create_plot(data)
    return render_template('plot.html', plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
