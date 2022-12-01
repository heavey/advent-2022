import sys

def main():
	m, s = [0,0,0], 0
	
	for line in sys.stdin:
		line = line.strip()
		if line  == '':
			s = 0
			continue

		s += int(line)
		for i, x in enumerate(m):
			if s > x:
				m[i] = s
				if i > 0:
					m[i-1] = x

	print(sum(m))


if __name__ == '__main__':
	main()
