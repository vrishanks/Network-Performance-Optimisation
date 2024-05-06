def adjust_qos(latency, throughput):
    if latency > 100:
        print("High latency detected. Increasing priority of real-time traffic.")
    if throughput < 100 * 1024:
        print("Low throughput detected. Adjusting bandwidth allocation.")

if __name__ == "__main__":
    adjust_qos(120, 80 * 1024)