import sys
import math

x = float(sys.argv[1])
q = float(sys.argv[2])
b = float(sys.argv[3])


f1 = 1 / (b * math.sqrt(2 * math.pi)) * math.exp(-((x - q) ** 2) / 2 * (b ** 2))
print(f1)
