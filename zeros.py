from math import log, floor

def my_zeros(n):
    
    z = 0
    if n == 0:
        pass
    else:
        k_max = floor(log(n, 5))
        for k in range(k_max):
            z = z + floor(n / (5 ** (k+1)))

    return z

def top_zeros(n):
  x = n/5
  return x+zeros(x) if x else 0