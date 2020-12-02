inputData = [
	1721,
	979,
	366,
	299,
	675,
	1456
]

def brute_force():
	input_len = len(inputData)
	found = False
	for i, num in enumerate(inputData):
		if (found):
			break
		if (i+1 == input_len):
			print("Could not find the two numbers")
			break
		for j, second_num in enumerate(inputData[i+1:input_len]):
			if (num + second_num == 2020):
				found = True
				print(f'{num} + {second_num} = 2020')
				print(f'{num} * {second_num} = {num*second_num}')
				break
		

# brute_force()

def memoization():
	hashed = set([])
	f = open('./2020_input.txt', 'r')
	for line in f.readlines():
		num = int(line)
		second_num = 2020-num
		if second_num in hashed:
			print(f'{num} + {second_num} = 2020')
			print(f'{num} * {second_num} = {num*second_num}')
			break
		hashed.add(num)

memoization()

# three entries

def brute_force_three_entries():
	inputData = []
	index = 0
	f = open('./2020_input.txt', 'r')
	for line in f.readlines():
		inputData.append(int(line))
		index = index+1

	input_len = len(inputData)
	found = False
	for i, num in enumerate(inputData):
		for j, second_num in enumerate(inputData[i+1:input_len]):
			for k, third_num in enumerate(inputData[j+1:input_len]):
				if (num + second_num + third_num == 2020):
					found = True
					print(f'{num} + {second_num} + {third_num}= 2020')
					print(f'{num} * {second_num} * {third_num} = {num*second_num*third_num}')
					break
brute_force_three_entries()