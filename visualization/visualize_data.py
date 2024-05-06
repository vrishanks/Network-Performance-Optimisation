import matplotlib.pyplot as plt
import pandas as pd

def plot_traffic(file_path):
    df = pd.read_csv(file_path)

    if 'Duration' in df.columns:
        df['Duration'] = pd.to_datetime(df['Duration'])
        df.set_index('Duration', inplace=True)
    else:
        print("Duration column not found. Make sure your CSV has a 'Duration' column.")

    plt.figure(figsize=(10, 5))
    if 'Bytes' in df.columns:
        df['Bytes'].plot(kind='line')
        plt.title('Network Traffic Over Time')
        plt.xlabel('Duration')
        plt.ylabel('Bytes')
        plt.show()
    else:
        print("Bytes column not found. Make sure your CSV includes a 'Bytes' column.")

if __name__ == "__main__":
    file_path = 'data/netflow_data.csv'
    plot_traffic(file_path)
