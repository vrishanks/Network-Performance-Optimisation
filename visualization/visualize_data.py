import matplotlib.pyplot as plt
import pandas as pd

def plot_traffic(file_path, output_file):
    df = pd.read_csv(file_path)

    plt.figure(figsize=(10, 5))
    if 'Bytes' in df.columns:
        x_values = range(len(df))
        plt.plot(x_values, df['Bytes'], color='blue')
        plt.scatter(x_values, df['Bytes'], color='black', marker='o')
        plt.title('Network Traffic Over Time')
        plt.xlabel('Duration')
        plt.ylabel('Bytes')
        plt.savefig(output_file)
        plt.close()
    else:
        print("Bytes column not found. Make sure your CSV includes a 'Bytes' column.")

if __name__ == "__main__":
    file_path = 'data/network_data.csv'
    output_file = 'network_traffic.png'
    plot_traffic(file_path, output_file)
