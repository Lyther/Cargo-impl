import sys

uid = 1

def main(file, line_number):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()

	vehicle_number = int(lines[2].split(' ')[1].strip())
	customer_number = int(lines[3].split(' ')[1].strip())
	vehicle_lines = par_vehicle(lines, vehicle_number, line_number)
	customer_lines = par_customer(lines, vehicle_number, customer_number, line_number)

	f = open(file, 'w')
	print(lines[0], lines[1], file=f, sep='', end='')
	print('VEHICLES', len(vehicle_lines), file=f)
	print('CUSTOMERS', len(customer_lines), file=f)
	print('\nID\tORIGIN\tDEST\tQ\tEARLY\tLATE', file=f)
	for line in vehicle_lines:
		print(line, file=f, end='')
	for line in customer_lines:
		print(line, file=f, end='')
	f.close()

def par_vehicle(lines, vehicle_number, line_number):
	global uid
	par = []
	for i in range(6, 6 + vehicle_number):
		values = lines[i].split('\t')
		origin = int(values[1].strip())
		dest = int(values[2].strip())
		if dest == -1 or (line_number == 0 and origin < dest) or (line_number == 1 and origin > dest):
			line = str(uid) + '\t' + values[1] + '\t' + values[2] + '\t' + values[3] + '\t' + values[4] + '\t' + values[5]
			uid = uid + 1
			par.append(line)
	return par

def par_customer(lines, vehicle_number, customer_number, line_number):
	global uid
	par = []
	for i in range(6 + vehicle_number, 6 + vehicle_number + customer_number):
		values = lines[i].split('\t')
		origin = int(values[1].strip())
		dest = int(values[2].strip())
		if (line_number == 0 and origin < dest) or (line_number == 1 and origin > dest):
			line = str(uid) + '\t' + values[1] + '\t' + values[2] + '\t' + values[3] + '\t' + values[4] + '\t' + values[5]
			uid = uid + 1
			par.append(line)
	return par

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python partition.py <file_name> <line_number>")
		print("\t<file_name> is the instance file location.")
		print("\t<line_number> can be 0 or 1, indicate different directions.")
	else:
		main(sys.argv[1], int(sys.argv[2]))