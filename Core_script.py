def get_IP_from_MAC(MAC):

	import netmiko
	import json

	# Temporarily commented out to deal with silly debugging issues on the core. Sigh.

	connection = netmiko.ConnectHandler(ip='Core1.lint', device_type='cisco_nxos', 
									username='hmussa', password='Wrx90Sti!')

	ip_arp_reply = connection.send_command('show ip arp Vlan12')
	connection.disconnect()


	rack_name = "r08r10"
	port_try = 35. #port number that your 
	found_mac = ""
	# Strip out the stupid header information that we do not need
	ip_arp_strip_header = ip_arp_reply.split('Interface')

	# Split the rows from eachother
	ip_arp_rows = ip_arp_strip_header[1].strip().split('\n')

	#Create a blank table to prepare for our final output
	ip_arp_table = []

	# Run each row through the loop and split into collumns. Append those collumns to the final list
	for row in ip_arp_rows:
		collumn = row.split()
		ip_arp_table.append(collumn)

	# Old stuff we used for figuring out how split works.
	#ip_arp_single_collumn1 = ip_arp_rows[1].split()
	#print ip_arp_single_collumn1
	#ip_arp_table.append(ip_arp_single_collumn1)

	#ip_arp_single_collumn2 = ip_arp_rows[2].split()
	#print ip_arp_single_collumn2
	#ip_arp_table.append(ip_arp_single_collumn2)

	#Some print debugs
	#print ip_arp_table
	#print ip_arp_table[0][2]

	# Now lets print out one entire collumn from our final table
	for row in ip_arp_table: 
		if row[2] == MAC:
			result = row[0] + " is associated with this MAC address: " + row[2]
			return result
				 #located_pdu_ipv4 + row[0]

	#for row in ip_arp_table:
	
	#	print row[0]
	#print ip_arp_table[0][0]
	#print ip_arp_table[1][0]
	#print ip_arp_table[2][0]
	#print ip_arp_table[3][0]
	#print ip_arp_table[4][0]

	#ip_arp_columns = ip_arp_row.split()
	#print ip_arp_columns[1]

	#ip_arp_columns = ip_arp_reply.split('Address')
	#ip_arp_columns = ip_arp_columns[1].split('\n')

	#print ip_arp_row[1]

	#print fo
	#for IP in fo:
	#		print IP.split('#')[0]
	
	#results = get_IP_from_MAC('ip_arp_reply')
	#my_list = results.split()
	#IP_addr = str(my_list[1])
	#Print('just before return')
	#return IP_addr	
	

 