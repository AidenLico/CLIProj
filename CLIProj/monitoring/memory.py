#####################################################

### monitoring/memory.py
### Author: Aiden Lico
### Date: 31/08/2026
### Last Updated: 31/08/2026

#####################################################

import psutil

## Testing functions
# print(psutil.virtual_memory())

# memory = psutil.virtual_memory()

# print(memory.total)
# print(memory.available)
# print(memory.percent)
# print(memory.used)
# print(memory.free)

def get_mem_statistics():
    memory = psutil.virtual_memory()
    return {
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "free": memory.free,
        "percent": memory.percent
    }
