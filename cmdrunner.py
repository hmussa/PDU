def get_mac_addr_from_TORS(TOR,Port):

	import netmiko
	import json

	connection = netmiko.ConnectHandler(ip=TOR, device_type='cisco_ios', 
									username='hmussa', password='Wrx90Sti!')
	#print(connection.send_command('show mac address-table | inc Gi1/0/35'))
	con = connection.send_command('show mac address-table | inc ' + Port)
	#Port36 = connection.send_command('show mac address-table | inc Gi1/0/36')
	connection.disconnect()
	#r = get_mac_addr_from_TORS('r08r15-tors.sjc23.lint', 'Gi1/0/35')
	my_list = con.split()
	mac_address = str(my_list[1])
	#print(r)
	#r = get_mac_addr_from_TORS('r08r15-tors.sjc23.lint', 'Gi1/0/36')
	return mac_address





