import pandas as pd

def analyze_netflow(file_path):
    df = pd.read_csv(file_path)
    high_traffic_flows = df[df['Bytes'] > 1000000]
    return high_traffic_flows

if __name__ == "__main__":
    file_path = '../../data/netflow_data.csv'
    high_traffic = analyze_netflow(file_path)
    print(high_traffic)