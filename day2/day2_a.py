import re
def part_1():
	f = open('./day2_input', 'r')
	valid_passwords = 0
	for line in f.readlines():
		line_inputs = re.split('-| | |: |\n', line)
		min, max = int(line_inputs[0]), int(line_inputs[1])
		target = line_inputs[2]
		password = line_inputs[3]
		target_counter = 0
		for c in password:
			if c == target:
				target_counter += 1
		if target_counter >= min and target_counter <= max:
				valid_passwords += 1
	print(f'valid_passwords = {valid_passwords}')


part_1()

def part_2():
	f = open('./day2_input', 'r')
	valid_passwords = 0
	for line in f.readlines():
		line_inputs = re.split('-| | |: |\n', line)
		pos1, pos2 = int(line_inputs[0]), int(line_inputs[1])
		target = line_inputs[2]
		password = line_inputs[3]
		target_counter = 0
		if (password[pos1-1] == target):
			target_counter += 1
		if (password[pos2-1] == target):
			target_counter += 1
		if target_counter == 1:
				valid_passwords += 1
	print(f'valid_passwords = {valid_passwords}')
part_2()