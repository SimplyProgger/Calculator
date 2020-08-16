# Calculator by SimplyProgger. Version 0.0

line = str(input())

total = 0
count_mark = 0
previous_mark = 0
count = 0


for symbol in line:
	plus = False
	minus = False
	multiply = False
	divide = False
	try:
		number = int(symbol)
		previous_mark += 1
	except ValueError:
		print(symbol)
		if count_mark == 0:
			total = int(line[:count])
			count_mark += 1

	count += 1



print(total)