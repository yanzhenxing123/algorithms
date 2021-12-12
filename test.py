import math

sin_60 = math.sqrt(3) / 2
sin_30 = 0.5
print(sin_60)

x = complex(sin_30, sin_60) ** (1 / 3)
print((x + 1 / x).real)
