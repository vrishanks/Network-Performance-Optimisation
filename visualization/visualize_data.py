import matplotlib.pyplot as plt
import pandas as pd

def plot_traffic(file_path, output_file):
    df = pd.read_csv(file_path)

    plt.figure(figsize=(10, 5))
    if 'Bytes' in df.columns:
        # Generate x-axis values from the range of the DataFrame length
        x_values = range(len(df))
        plt.plot(x_values, df['Bytes'], color='blue')  # Set line color to blue
        plt.scatter(x_values, df['Bytes'], color='black', marker='o')  # Add black dots for each data point
        plt.title('Network Traffic Over Time')
        plt.xlabel('Duration')  # Use index as x-axis label
        plt.ylabel('Bytes')
        plt.savefig(output_file)  # Save plot as PNG
        plt.close()  # Close the plot to prevent displaying in Jupyter Notebook
    else:
        print("Bytes column not found. Make sure your CSV includes a 'Bytes' column.")

if __name__ == "__main__":
    file_path = 'data/network_data.csv'
    output_file = 'network_traffic.png'  # Specify the output file path
    plot_traffic(file_path, output_file)
