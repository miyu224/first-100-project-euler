TARGET = 4000000

def compute():
	ans = 0
	x = 1
	y = 2
	while x <= TARGET:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)

if __name__ == "__main__":
	print(compute())