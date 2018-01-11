def upgrading_AP8941(IP):
	import ftplib
	filename = "apc_hw05_bootmon_108.bin"
	ftp =ftplib.FTP(IP)
	ftp.login(user = "apc", passwd = "apc")
	myfile = open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_bootmon_108.bin', 'rb')
	ftp.storbinary('STOR ' + filename, myfile)
	ftp.quit()

	import time
	time.sleep(30)

	import ftplib
	filename = "apc_hw05_aos_646.bin"
	ftp =ftplib.FTP(IP)
	ftp.login(user = "apc", passwd = "apc")
	myfile = open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_aos_646.bin', 'rb')
	ftp.storbinary('STOR ' + filename, myfile)
	ftp.quit()

	import time
	time.sleep (60)

	import ftplib
	filename = "apc_hw05_rpdu2g_646.bin"
	ftp =ftplib.FTP(IP)
	ftp.login(user = "apc", passwd = "apc")
	myfile = open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_rpdu2g_646.bin', 'rb')
	ftp.storbinary('STOR ' + filename, myfile)
	ftp.quit()	

	#def grabFile():
	#	fileName = 'apc_hw05_bootmon_108.bin'
	#	localfile = open(PDU, 'wb')
	#	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	#	ftp.quit()
	#	localfile.close()

	#def placeFile():
	#	fileName ='apc_hw05_bootmon_108.bin'
	#	ftb.storbinary('STOR ' + filename, open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_bootmon_108.bin', 'rb'))
	#	ftp.quit()


# Test Section
#upgrading_AP8941('100.119.15.231')