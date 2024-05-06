import matplotlib.pyplot as plt
import pandas as pd

def plot_traffic(file_path):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(10, 5))
    df['Bytes'].plot(kind='line')
    plt.title('Network Traffic Over Time')
    plt.xlabel('Time')
    plt.ylabel('Bytes')
    plt.show()

if __name__ == "__main__":
    file_path = '../../data/netflow_data.csv'
    plot_traffic(file_path)