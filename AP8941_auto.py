def main(child):#pexpect.pty_spawn.spawn child):
#def main():
	import pexpect
	#AP8941
	#pdu_ipv4 = "100.119.15.195"
	prompt_username = 'User Name : '
	#default_username = 'apc\r'
	prompt_password = 'Password  : '
	#default_password = 'apc\r'
	prompt_web = 'web'
	default_web = 'web '
	prompt = 'apc>'
	default = 'apc>'

	def debugPrint(text, mode = 1):
		if mode is 1:
			if isinstance(text, str):
				print (text)
			elif isinstance (text, bytes):
				print (str(text, 'utf-8'))
		return

	#child = pexpect.spawn('telnet ' + pdu_ipv4)


	#child.expect(prompt_username)
	#debugPrint(child.before)
	#child.send('apc\r')
	#debugPrint("**** We sent: " + 'apc\r' )

	#child.expect(prompt_password)
	#debugPrint(child.before)
	#child.send('apc\r')
	#debugPrint("**** We sent: " + 'apc\r' )

	#LCD Blink
	#child.expect(prompt)
	#debugPrint(child.before)
	child.send('lcdblink 1: 8\r')
	debugPrint("**** We sent:" + 'lcdblink 1: 8' )

	version = b'Application Module\r\n----------\r\nName:  \t\t\trpdu2g\r\nVersion: \t\tv6.4.4'
	child.expect(prompt)
	debugPrint(child.before)
	child.send('about\r')
	debugPrint("**** We sent: " + 'about')
	child.expect(prompt)
	if version in child.before:
		debugPrint("**** Version correct")
	else:
		debugPrint("**** Version incorrect")
	child.send('\r')

	# Web Setting
	child.expect(prompt)
	debugPrint(child.before)
	child.send('web -s enable\r')
	debugPrint("**** We sent: " + 'web -s enable' )

	child.expect(prompt)
	debugPrint(child.before)
	child.send('web -mp TLS1.2\r')
	debugPrint("**** We sent:" + 'web -mp TLS1.2')

	#DNS Setting
	child.expect(prompt)
	debugPrint(child.before)
	child.send('dns -d sjc23.lint\r')    
	debugPrint("**** We sent: " + 'dns -d sjc23.lint' )

	child.expect(prompt)
	debugPrint(child.before)
	child.send('dns -n sjc23.lint\r')
	debugPrint("**** We sent: " + 'dns -n sjc23.lint' )

	child.expect(prompt)
	debugPrint(child.before)
	child.send('dns -h R08R15 PDU-2\r')
	debugPrint("**** We sent:" + 'dns -h R08R15 PDU-2' )

	#Console setting
	child.expect(prompt)
	debugPrint(child.before)
	child.send('console -s enable\r')
	debugPrint("**** We sent:" + 'console -s enable' )

	#Date Setting
	child.expect(prompt)
	debugPrint(child.before)
	child.send('date -z -08:00\r')
	debugPrint("**** We sent:" + 'date -z -08:00' )

	#System
	child.expect(prompt)
	debugPrint(child.before)
	child.send('system -n R08R15 PDU-2\r')
	debugPrint("**** We sent:" + 'R08R15 PDU-2')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('system -l R08R15\r')
	debugPrint("**** We sent:" + 'R08R15')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('system -c Haroon Mussa\r')
	debugPrint("**** We sent:" + 'Haroon Mussa')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('user -n admin -pw 2GFxUvV87dMZQd49\r')
	debugPrint("**** We sent:" + 'user -n admin -pw 2GFxUvV87dMZQd49')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('user -add Administrator\r')
	debugPrint("**** We sent:" + 'useradd Administrator')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('user -n Administrator -pw 2GFxUvV87dMZQd49\r')
	debugPrint("**** We sent:" + 'user -n Administrator -pw 2GFxUvV87dMZQd49')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('user -n Administrator -pe Administrator\r')
	debugPrint("**** We sent:" + 'user -n Administrator -pe Administrator')

	child.expect(prompt)
	debugPrint(child.before)
	child.send('reboot\r')
	debugPrint("**** We sent:" + 'reboot')



