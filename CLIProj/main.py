#####################################################

### main.py
### Author: Aiden Lico
### Date: 28/08/2026
### Last Updated: 31/08/2026

#####################################################

from monitoring.cpu import get_cpu_metrics
from monitoring.memory import get_mem_statistics


# cpu_metrics = get_cpu_metrics(1)
# print(f"CPU Usage: {cpu_metrics["usage"]}%")
# print(f"CPU Cores: {cpu_metrics["physical"]}")
# core_usage = cpu_metrics["per_core"]
# for i in range (cpu_metrics["physical"]):
#     print (f"Core {i+1}: {core_usage[i]}")
# print(f"Logical CPUs: {cpu_metrics["logical"]}")
# print(f"Frequency: {cpu_metrics["freq"].current}")

mem_statistics = get_mem_statistics()
p
