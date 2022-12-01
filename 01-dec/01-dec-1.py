import sys

def main():
	m, s = 0, 0
	
	for line in sys.stdin:
		line = line.strip()
		if line == '':
			s = 0
			continue
		
		s += int(line)
		m = s if s > m else m

	print(m)	


if __name__ == '__main__':
	main()
