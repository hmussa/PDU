def main(child):
	import pexpect
	#AP7941
	#pdu_ipv4 = '100.119.15.215'
	prompt_username = 'User Name : '
	#default_username = 'apc\r'
	prompt_password = 'Password  : '
	#default_password = 'apc\r'
	prompt_network = 'Network'
	default_network = '2\r'
	prompt_hostname = 'Host Name : '
	default_hostname =  'R07R12-PDU-2\r'
	prompt_contact = 'Contact : '
	default_contact = '2\r'
	prompt_name = 'Name : '
	default_name = '1\r'
	prompt_location = 'Location : '
	default_location = '3\r'
	prompt_indentification = 'Identification'
	default_indetification = '2\r'
	prompt_primary_ntp_server = 'Primary NTP Server : '
	default_primary_ntp_server = '1\r'
	prompt_secondary_ntp_server = 'Secondary NTP Server : '
	default_secondary_ntp_server = '2\r'
	prompt_Select_GMT_Offset_from_menu = 'Select GMT Offset from menu : '
	default_Select_GMT_Offset_from_menu = ''
	prompt_Primary_server = 'Primary Server : '
	default_Primary_server = '2\r'
	prompt_Primary_server_secret = 'Primary Server Secret : '
	default_Primary_server_secret = '3'
	prompt_secondary_server = 'Secondary Server : '
	default_secondary_server = '5\r'
	prompt_secondary_server_secret = 'Secondary Server Secret : '
	default_secondary_server_secret = '6\r'
	prompt_Enter_Current_Admin_PW = 'Enter current Administrator password : '
	default_Enter_Current_Admin_PW = '1\r'
	prompt_Enter_new_Administrator_user_name = 'Enter new Administrator user name'
	default_Enter_new_Administrator_user_name = '<ENTER> to skip : '
	prompt_Enter_new_Administrator_password = 'Enter new Administrator password'
	default_Enter_new_Administrator_password = '<ENTER> to skip : '
	prompt_IP_Address_of_target_to_upgrade = 'IP Address of target to upgrade: '
	default_IP_Address_of_target_to_upgrade = '<Enter>\r'
	prompt_Action = 'Action: '
	default_Action = 'Action: '
	prompt = '> '
	default_prompt ='> '
	def debugPrint(text, mode = 1):
		if mode is 1:
			if isinstance(text, str):
				print (text)
			elif isinstance (text, bytes):
				print (str(text, 'utf-8'))
		return

	# Login stuff
	#child = pexpect.spawn('telnet ' + pdu_ipv4)
	#print ("Starting")

	#child.expect(prompt_username)
	#debugPrint(child.before)
	#child.send(default_username)
	#debugPrint("**** We sent: " + default_username )

	#child.expect(prompt_password)
	#debugPrint(child.before)
	#child.send(default_password)
	#debugPrint("**** We sent: " + default_password )

	#check version
	#Version = b'Application Module\r\n----------\r\nName:  \t\t\trpdu2g\r\nVersion: \t\tv3.9.2'
	#child.expect(prompt)
	#debugPrint(child.before)
	#child.send('about\r')
	#debugPrint("**** We sent: " + 'about')
	#child.expect(prompt)
	#if version in child.before:
		#debugPrint("**** Version correct")
	#else:
		#debugPrint("**** Version incorrect")
	#child.send('\r')

	#Upgrade the version

	#child.expect(prompt_IP_Address_of_target_to_upgrade)
	#debugPrint(child.before)
	#child.send('\r')
	#debugPrint("**** We sent:" + '')

	#child.expect(prompt_username)
	#debugPrint(child.before)
	#child.send('apc\r')
	#debugPrint("**** We sent:" + 'apc')

	#child.expect(prompt_password)
	#debugPrint(child.before)
	#child.send('apc\r')
	#debugPrint("**** We sent:" + 'apc')

	#child.expect(prompt_Action)
	#debugPrint(child.before)
	#child.send('1\r')
	#debugPrint("**** We sent:" + '1')

	#Set Name, Contact, Location

	#child.expect(prompt)
	#debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('1\r')
	debugPrint("**** We sent:" + '1')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('1\r')
	debugPrint("**** We sent:" + '1')

	child.expect(prompt_hostname)
	debugPrint(child.before)
	child.send('R07R12-PDU-2\r')
	debugPrint("**** We sent:" + 'R07R12-PDU-2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('9\r')
	debugPrint("**** We sent:" + '9')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("We sent: " + '3')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent: " + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent: " + '2')

	child.expect(prompt_contact)       
	debugPrint(child.before)
	child.send('Haroon Mussa\r')
	debugPrint("**** We sent:" + 'Haroon Mussa')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('4\r')
	debugPrint("**** We sent:" + '4')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')
	
	#set the location

	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("We sent: " + '3')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent: " + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("We sent: " + '3')

	child.expect(prompt_location)       
	debugPrint(child.before)
	child.send('R07R12\r')
	debugPrint("**** We sent:" + 'R07R12')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('4\r')
	debugPrint("**** We sent:" + '4')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	#set NTP.                     <----Will multiple lines work w/out back tracking 
	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("We sent: " + '3')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("**** We sent: " + '3')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('1\r')
	debugPrint("**** We sent:" + '1')

	child.expect(prompt_primary_ntp_server)
	debugPrint(child.before)
	child.send('100.119.4.17\r')
	debugPrint("**** We sent:" + '100.119.4.17')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt_secondary_ntp_server)
	debugPrint(child.before)
	child.send('100.119.4.18\r')
	debugPrint("**** We sent:" + '100.119.4.18')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("**** We sent:" + '3')

	child.expect(prompt_Select_GMT_Offset_from_menu)
	debugPrint(child.before)
	child.send('5\r')
	debugPrint("**** We sent:" + '5')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('5\r')
	debugPrint("**** We sent:" + '5')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('6\r')
	debugPrint("**** We sent:" + '6')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('1\r')
	debugPrint("**** We sent:" + '1')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('1\r')
	debugPrint("**** We sent:" + '1')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	#Radius
	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("**** We sent:" + '3')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('5\r')
	debugPrint("**** We sent:" + '5')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('2\r')
	debugPrint("**** We sent:" + '2')

	child.expect(prompt_Primary_server)
	debugPrint(child.before)
	child.send('100.119.4.41\r')
	debugPrint("**** We sent:" + '100.119.4.41')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('3\r')
	debugPrint("**** We sent:" + '3')

	child.expect(prompt_Primary_server_secret)
	debugPrint(child.before)
	child.send('2GFxUvV87dMZQd49\r')
	debugPrint("**** We sent:" + '2GFxUvV87dMZQd49')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('5\r')
	debugPrint("**** We sent:" + '5')

	child.expect(prompt_secondary_server)
	debugPrint(child.before)
	child.send('100.119.4.42\r')
	debugPrint("**** We sent:" + '100.119.4.42')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('6\r')
	debugPrint("**** We sent:" + '6')

	child.expect(prompt_secondary_server_secret)
	debugPrint(child.before)
	child.send('2GFxUvV87dMZQd49\r')
	debugPrint("**** We sent:" + '2GFxUvV87dMZQd49')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('8\r')
	debugPrint("**** We sent:" + '8')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('\x1b')
	debugPrint("**** We sent:" + '\x1b')

	#User & PW
	#child.expect(prompt)
	#debugPrint(child.before)
	#child.send('3\r')
	#debugPrint("We sent: " + '3')

	#child.expect(prompt)
	#debugPrint(child.before)
	#child.send('1\r')
	#debugPrint("**** We sent: " + '1')

	#child.expect(prompt)
	#debugPrint(child.before)
	#child.send('1\r')
	#debugPrint("We sent: " + '1')

	#child.expect(prompt_Enter_Current_Admin_PW)
	#debugPrint(child.before)
	#child.send('apc\r')
	#debugPrint("****We sent:" + 'apc')

	#child.expect(prompt_Enter_new_Administrator_user_name)
	#debugPrint(child.before)
	#child.send('admin\r')
	#debugPrint("****We sent:" + 'admin')

	#child.expect(prompt_Enter_new_Administrator_password)
	#debugPrint(child.before)
	#child.send('2GFxUvV87dMZQd49\r')
	#debugPrint("****We sent:" + '2GFxUvV87dMZQd49')








