#####################################################

### main.py
### Author: Aiden Lico
### Date: 28/08/2026
### Last Updated: 28/08/2026

#####################################################

from monitoring.cpu import *

print(f"CPU Usage: {cpu_usage(1)}%")
print(f"CPU Cores: {cpu_cores(False)}")
core_usage = cpu_usage_pcore(1)
for i in range (cpu_cores(False)):
    print (f"Core {i+1}: {core_usage[i]}")
print(f"Logical CPUs: {cpu_cores(True)}")
print(f"Frequency: {cpu_freq()}")
