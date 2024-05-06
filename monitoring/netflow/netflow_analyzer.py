import pandas as pd

def analyze_netflow(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df['Bytes'] = pd.to_numeric(df['Bytes'], errors='coerce')
    high_traffic_flows = df[df['Bytes'] > 10000]
    return high_traffic_flows

if __name__ == "__main__":
    file_path = 'data/netflow_data.csv'
    high_traffic = analyze_netflow(file_path)
    if high_traffic.empty:
        print("No high traffic flows found.")
    else:
        print(high_traffic)