import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def analyze_traffic(df):
    return df[df['Bytes'] > 8000]

if __name__ == "__main__":
    df = load_data('data/network_data.csv')
    result = analyze_traffic(df)
    print(result)