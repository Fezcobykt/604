#Fezco
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import socket

# Obtain computer information
computer_name = socket.gethostname()
ip_address = socket.gethostbyname(computer_name)

# 导入 CSV 文件
dss_data = pd.read_csv('dss_data.csv')
dss_user_access = pd.read_csv('dss_user_access.csv')

# 提取所需数据
months = pd.to_datetime(dss_data['Month'])
storage_growth = dss_data['Storage_Growth'].values
query_times = dss_data['Query_Times'].values
user_types = dss_user_access['User_Type'].values
access_percent = dss_user_access['Access_Percent'].values

# Create subgraph
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Figure 1: Line Chart (Storage Growth)
ax1.plot(months, storage_growth, marker='o', linestyle='-', color='darkblue')
ax1.set_xlabel('Month')
ax1.set_ylabel('Storage (GB)')
ax1.set_title('Data Warehouse Storage Growth Over 12 Months machine:Fezco IP:10.50.80.30')
ax1.grid(True, linestyle='--', alpha=0.7)
# Rotate only the x-axis label of the ax1 subgraph
ax1.tick_params(axis='x', rotation=45)

# Figure 2: Pie Chart (User Access Distribution)
ax2.pie(access_percent, labels=user_types, autopct='%1.1f%%', colors=['#4CAF50', '#FFC107', '#FF5722'])
ax2.set_title('DSS User Access Distribution achine:Fezco IP:10.50.80.30')

plt.tight_layout()

# Filter criteria: Months with a response time exceeding 1.5 seconds
filtered_months = [months[i] for i, t in enumerate(query_times) if t > 1.5]
filtered_times = query_times[query_times > 1.5]

# Figure 3: Bar Chart (Slow Query Distribution)
plt.figure(figsize=(12, 6))
plt.bar(filtered_months, filtered_times, color='crimson')
plt.xlabel('Month')
plt.ylabel('Query Time (Seconds)')
plt.title('OLAP Queries with Response Time > 1.5 Seconds machine:Fezco IP:10.50.80.30')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()