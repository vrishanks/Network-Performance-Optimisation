# Network-Performance-Optimisation 

Project Overview:

The goal of this project is to improve network performance by monitoring traffic flows, identifying high utilization links, and automatically adjusting quality of service (QoS) settings or other parameters to optimize traffic handling. 

This project can be divided into several phases:
`Network Monitoring`
`Data Analysis and Bottleneck Identification`
`Automated Configuration Changes`
`Testing and Validation`

## Setup Instructions
1. Install Python dependencies: `pip install -r requirements.txt`.
2. Set up SNMP and NetFlow on your network devices.
3. Adjust Ansible playbooks according to your network configuration.

## Usage
Run Python scripts in the `monitoring/` directory to collect network data. Use Ansible playbooks in the `ansible/` directory to apply configuration changes.
Tools and Technologies:

Python: For scripting and automation.

SNMP (Simple Network Management Protocol): For collecting device and traffic data.
NetFlow/sFlow/IPFIX: For detailed traffic analysis.
Ansible: For automated configuration deployment.
Grafana and Prometheus (or InfluxDB): For data visualization and monitoring.

Network Monitoring:

Set up monitoring on network devices using SNMP and NetFlow to collect metrics such as bandwidth utilization, packet loss, and latency.

Data Analysis and Bottleneck Identification:

Analyze the collected data to identify high traffic flows and congested links.

Traffic Analysis (using Python and NetFlow data):

You might use a NetFlow collector and then analyze the data using Python, or directly stream data to a database and use queries to identify heavy traffic flows.

Automated Configuration Changes:

Based on the analysis, automatically adjust network device configurations to optimize performance.

Testing and Validation:

Validate the performance improvements through before-and-after tests using traffic generators and network analysis tools.

Project Completion:

Compile results and analyze the effectiveness of the optimizations. Document configurations, scripts, and methodologies used in the project. Prepare a presentation or report detailing the project findings, methodologies, and impact on network performance. This project provides hands-on experience with real-world tools and techniques used in network management and optimization, offering both learning and practical benefits.
