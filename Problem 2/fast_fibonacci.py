# Follow up problem when dig in Problem 2 Euler
# More infomation: https://www.nayuki.io/page/fast-fibonacci-algorithms
# Prove: https://math.stackexchange.com/questions/1124590/need-help-understanding-fibonacci-fast-doubling-proof

# Formular:

# F(2k)=F(k)[2F(k+1)−F(k)]
# F(2k+1)=F(k+1)^2+F(k)^2

# Implementation:

def fibonacci(n):
  if n < 0:
    raise ValueError("Negative arguments not implemented")
  return compute_fib(n)[0]

def compute_fib(n):
  if (n == 0):
    return (0, 1)
  else:
    a, b = compute_fib(n//2)
    c = a * (2 * b - a)
    d = b**2 + a**2
    if n % 2 == 0:
      return (c, d)
    else:
      return (d, c + d)

if __name__ == "__main__":
  n = int(input("Enter the nth fibonacci number to calculate: "))
  print(fibonacci(n))
