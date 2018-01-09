def get_intended_IP_add(LOC,Port):

	import csv

	with open('Lint_IPs.csv') as f:
		reader = csv.reader(f)
		for row in reader:
			if row[0].strip() == LOC.strip():
				if Port == 'PDU1':
					return row[1]
				elif Port == 'PDU2':
					return row[2]
#get_intended_IP_add('R08R15','PDU1')
	return "Fail"