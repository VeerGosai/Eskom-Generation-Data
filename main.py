import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_from_csv(csv_file):
    data = pd.read_csv(csv_file)
    sns.set(style="whitegrid")
    sns.barplot(x="Category", y="Value", data=data)
    plt.show()

if __name__ == "__main__":
    csv_file = "data.csv"
    plot_from_csv(csv_file)

