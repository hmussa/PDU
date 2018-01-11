def upgrading_AP7941(IP):
	import ftplib
	filename = "apc_hw02_aos_202.bin"
	ftp =ftplib.FTP(IP)
	ftp.login(user = "apc", passwd = "apc")
	myfile = open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_bootmon_108.bin', 'rb')
	ftp.storbinary('STOR ' + filename, myfile)
	ftp.quit()

	import time
	time.sleep(30)

	import ftplib
	filename = "apc_hw02_aos_392.bin"
	ftp =ftplib.FTP(IP)
	ftp.login(user = "apc", passwd = "apc")
	myfile = open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_aos_646.bin', 'rb')
	ftp.storbinary('STOR ' + filename, myfile)
	ftp.quit()

	import time
	time.sleep (60)

	import ftplib
	filename = "apc_hw02_rpdu_392.bin"
	ftp =ftplib.FTP(IP)
	ftp.login(user = "apc", passwd = "apc")
	myfile = open('/Users/solutionteam.test11/Desktop/apc_firmware/apc_hw05_rpdu2g_646.bin', 'rb')
	ftp.storbinary('STOR ' + filename, myfile)
	ftp.quit()	

# Test Section
upgrading_AP7941('100.119.15.167')